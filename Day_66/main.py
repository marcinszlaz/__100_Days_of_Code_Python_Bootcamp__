from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm.exc import UnmappedInstanceError
import random as r
import json

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
  pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  map_url: Mapped[str] = mapped_column(String(500), nullable=False)
  img_url: Mapped[str] = mapped_column(String(500), nullable=False)
  location: Mapped[str] = mapped_column(String(250), nullable=False)
  seats: Mapped[str] = mapped_column(String(250), nullable=False)
  has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
  has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
  has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
  can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
  coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
  def make_dictionary(self):
    dict_ = {column.name: getattr(self, column.name) for column in self.__table__.columns}
    print(json.dumps(dict_,indent=4,sort_keys = True))
    return dict_
    # self.__table__.columns it's black magic from flask sqlalchemy, this simplifies proces of fetching data from tables
    # instead of this you have write it cafe = db.session.execute(db.select(Cafe)).scalars().all()
    # jsonify("id":"cafe.id", "name":"cafe.name") etc., manually create dict for json

with app.app_context():
  db.create_all()

@app.route("/")
def home():
  return render_template("index.html")

# fetching random cafe
@app.route("/random",methods=['GET'])
def random():
  random_cafe = None
  with app.app_context():
    cafe_list= db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = r.choice(cafe_list)
  return jsonify(random_cafe.make_dictionary())

#fetching all cafe
@app.route('/all')
def all():
  cafe_list = db.session.execute(db.select(Cafe)).scalars().all()
  return jsonify([cafe.make_dictionary() for cafe in cafe_list])

# HTTP GET - Read Record
@app.route('/search')
def search():
  seeking_location = request.args.get('loc')
  found_location = db.session.execute(db.select(Cafe).where(Cafe.location == seeking_location)).scalar()
  if found_location:
    return jsonify(found_location.make_dictionary())
  else:
    return jsonify({"error": {"Not Found":"Sorry, we don\'t have a cafe at that location."}})

# HTTP POST - Create Record
# TODO create add_normal() - use request.form.get('name'),
#  add_json() - use request.get_json(), (it demand change curl -H...)
#  add_dict() - use request.form.to_dict()
@app.route('/add-normal', methods=['POST','GET'])
def add_normal():
  new_cafe = Cafe(
  can_take_calls = bool(request.form.get("can_take_calls")),
  coffee_price = request.form.get("coffee_price"),
  has_sockets = bool(request.form.get("has_sockets")),
  has_toilet = bool(request.form.get("has_toilet")),
  has_wifi = bool(request.form.get("has_wifi")),
  img_url = request.form.get("img_url"),
  location = request.form.get("location"),
  map_url = request.form.get("map_url"),
  name = request.form.get("name"),
  seats = request.form.get("seats")
  )
  with app.app_context():
    db.session.add(new_cafe)
    db.session.commit()
  return jsonify({"response":{"success":"Successfully added the new cafe."}})

@app.route('/add-json',methods=['POST'])
def add_json():
  # request.get_json() returns json payload and None
  # that's why you have to unpack **json_data as kwargs** for Cafe constructor
  json_data = request.get_json()
  new_cafe = Cafe(**json_data)
  with app.app_context():
    db.session.add(new_cafe)
    db.session.commit()
  return jsonify({"response":{"success":"Successfully added the new cafe."},
                  "payload":json_data})

@app.route('/add-dict',methods=['POST'])
def add_dict():
  vtc = {"0":False,"":False," ":False,"False":False,"false": False,"1":True,"true":True,"True":True,None:False}
  big_dict = request.form.to_dict()
  big_dict_cleared = {k:(vtc.get(v,v)) for k,v in big_dict.items()}
  new_cafe = Cafe(**big_dict_cleared)
  with app.app_context():
    db.session.add(new_cafe)
    db.session.commit()
  return jsonify({"response":{"success":"Successfully added the new cafe."},
                  "payload": big_dict_cleared})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:id_>', methods=['PATCH','GET'])
def update_price(id_):
  try:
    new_price = request.args.get('price')
  except AttributeError as ar:
    print(f'{ar}')
    return jsonify(error="Wrong price attribute"), 404
  else:
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id_)).scalar()
    if not cafe:
      return jsonify(error="Nothing Found"), 404
    cafe_dict = cafe.make_dictionary()
    cafe.coffee_price = new_price
    db.session.commit()
    cafe_dict_ = cafe.make_dictionary()
  return jsonify({"old_payload":cafe_dict,"payload_changed":{"status":"Success",
                "new_payload":cafe_dict_}}), 200

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
  api_key = "TopSecretAPIKey"
  if request.args.get('api_key') == api_key:
    try:
       cafe_to_del = db.get_or_404(Cafe,cafe_id)
    except AttributeError:
      return jsonify({"error":"Cafe with typed id not found"}), 404
    else:
      db.session.delete(cafe_to_del)
      db.session.commit()
      return jsonify(INFO="Cafe was successfully deleted"), 200
  else:
    return jsonify(ERROR="Sorry, that's not allowed. Make sure you have the correct api_key."),403


if __name__ == '__main__':
  app.run(debug=True)

