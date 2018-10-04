import os
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) == 0:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be a valid email address!")
    if len(request.form['first_name']) == 0:
        flash("First Name cannot be blank!")
    if len(request.form['last_name']) == 0:
        flash("Last Name cannot be blank!")
    if len(request.form['password']) == 0:
        flash("Password cannot be blank!")
    if len(request.form['confirm_password']) == 0:
        flash("Confirm Password cannot be blank!")
    if not request.form['first_name'].isalpha():
        flash("First name must not contain numbers")
    if not request.form['last_name'].isalpha():
        flash("Last name must not contain numbers")
    if len(request.form['password']) < 9:
        flash("Password must be more than 8 characters")
    if request.form['password'] != request.form['confirm_password']:
        flash("Password and Confirm Password must match")

    if '_flashes' in session.keys():
        return render_template("index.html")
    else:
        return redirect("/result")

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)