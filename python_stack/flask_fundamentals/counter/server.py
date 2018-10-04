import os
from flask import Flask, render_template, request, redirect, url_for, session

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
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def clearSession():
    session.clear()
    return redirect('/')

@app.route('/add2')
def addTwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)