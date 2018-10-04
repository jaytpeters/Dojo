import os
import random
import time
from datetime import datetime
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
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
    elif request.form['building'] == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
    else:
        gold = random.randint(-50,50)
        session['gold'] += gold
    
    today = datetime.now()
    todayFormatted = today.strftime("%Y/%m/%d %I:%M:%S %p")

    if gold > 0:
        session['activities'].append(f"<span class='earned'>Earned {gold} gold from the {request.form['building']}! ({todayFormatted})</span><br/>")
    else:
        session['activities'].append(f"<span class='lost'>Entered a casino and lost {gold*-1} gold ... Ouch! ({todayFormatted})</span><br/>")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)