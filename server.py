from flask import Flask, render_template, redirect, request, session, flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    return render_template("index.html")
#

# def hello_world():
#     return render_template('index.html')

@app.route('/results', methods=['POST'])
def validate():
    email = request.form['email']


    first_name = request.form['first_name']

    last_name = request.form['last_name']

    password = request.form['password']
    conf_password = request.form['conf_password']

    if len(request.form['email']) <1:
        flash("email cannot be blank")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("invalid email address")
    elif len(request.form['first_name']) < 1:
        flash("first name cannot be blank!")
        return redirect('/')
    elif len(request.form['last_name']) <1:
        flash("lastname cannot be blank")
        return redirect('/')
    elif len(request.form['email']) < 1:
       flash("password cannot be blank")
       return redirect('/')
    elif len(request.form['email']) <8:
       flash("password must be greater than 8 characters")
       return redirect('/')
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        return redirect('/')
    elif not password == conf_password:
        flash("Passwords must match")
        return redirect('/')
    else:
       flash("Success!")
       return redirect('/')
    # Here's the line that changed. We're rendering a template from a post route now.
    return render_template('index.html', first_name =first_name, last_name = last_name, email= email, password = password, conf_password= conf_password)

# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
