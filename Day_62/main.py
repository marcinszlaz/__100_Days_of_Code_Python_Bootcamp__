from flask import Flask, render_template
from flask_bootstrap import Bootstrap5 as bootstrap5
import csv,os,pathlib
from dotenv import load_dotenv
from cafe_form import CafeForm as cf

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = bootstrap5(app)

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add',methods=["GET","POST"])
def add_cafe():
    ignore = ('submit','csrf_token')
    form = cf()
    if form.validate_on_submit():
        values_list = [v for k,v in form.data.items() if k not in ignore]
        with open(file='cafe-data.csv', mode='a', encoding='utf-8', newline='') as csv_file:
            csv.writer(csv_file, delimiter=',', lineterminator='\r\n').writerow(values_list)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv("HOST_IP"), port=os.getenv("HOST_PORT"))
