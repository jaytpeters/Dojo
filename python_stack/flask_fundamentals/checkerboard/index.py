from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def defaultBoard():
    return render_template('index.html', width=8, height=8)

@app.route('/<width>/<height>')
def customBoard(width, height):
    return render_template('index.html', width=int(width), height=int(height))

if __name__ == "__main__":
    app.run(debug=True)