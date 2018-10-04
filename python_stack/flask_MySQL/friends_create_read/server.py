import os
from flask import Flask, render_template, request, redirect, url_for, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

### disable caching for static urls ###
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
######################################

@app.route('/')
def index():
    mysql = connectToMySQL('mydb')
    all_friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', data = all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
    mysql = connectToMySQL("mydb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)