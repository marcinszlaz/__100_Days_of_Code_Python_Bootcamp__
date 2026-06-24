from app import app
from app.forms import LoginForm
from flask import jsonify, render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Marcin'}
    title = 'FullCallendar'
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = title, user = user, posts = posts)


@app.route('/apiv1/req')
def req():
    return jsonify({'answer': 'Fuck you :-)'})


@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    title = 'Zaloguj się'
    if form.validate_on_submit():
        flash('Prośba o logowanie dla użytkownika {}, opcja zapamiętania: {}'        .format(form.username.data, 'Prawda' if form.remember_me.data == True        else 'Fałsz'))
        return redirect(url_for('index'))
    return render_template('login.html', form = form, title = title)


# at the beginning, this part started from line 21
# :9,18norm i# - this way you can handle multiline comments in vim
# :9,18norm x - delete one char (#), you can use visual too
# :9,21s/#/ - this also remove (substitiute) # to ` `
# v - visual :s/#// equal this above
# ctrl - y means YES for chosen tips from plugins in vim
# visual, :s/^#// using ^ like in xpath/css selector, first founded char
#            '''
#<html>
#    <head>
#       <title> Home Page - FullCallendar </title>
#    </head>
#    <body>
#        <h1>Hello, ''' +user['username']+ '''!</h1>
#    </body>
#</html>
#            '''


