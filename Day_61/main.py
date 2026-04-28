# pip install bootstrap-flask
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template,request
import os, pathlib
from dotenv import load_dotenv
from flask_form import MyForm as fm

dotenv_path=pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = f"{os.getenv("SECRET_KEY")}"
@app.route("/")
def home():
    form = fm()
    return render_template('index.html',form=form)

@app.route(rule="/login", methods=["POST","GET"])
def login():
    form = fm()
    form.validate_on_submit()
    # form.validate_on_submit() is EQUAL form.validate() == True and request.method == 'POST'
    user = 'admin@email.com'
    passw = '12345678'
    if form.validate() and request.method == 'POST':
        if user == form.email_.data and passw == form.password_.data:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    print('is_submitted',form.is_submitted())
    print('validate',form.validate())
    print('validate_on_submit',form.validate_on_submit())
    print('email',form.email_.data)
    print('password',form.password_.data)
    print('method',request.method)
    print('errors',form.errors)
    # if user get to site through GET method (input link or click href on main_page
    # flask render this page below
    return render_template(template_name_or_list = 'login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv("HOST_IP"),port=os.getenv("HOST_PORT"))
