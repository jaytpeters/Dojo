import os
import random
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
    if 'number' not in session:
        session["number"] = random.randrange(1,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'action' in request.form:
        session.clear()
        return redirect("/")
    else:
        if request.form['guess'].isdigit():
            session['guess'] = int(request.form['guess'])
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)