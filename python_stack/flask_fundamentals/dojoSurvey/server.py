import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

@app.route('/result', methods=['POST'])
def result():
    return render_template('result.html')

@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)