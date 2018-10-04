from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<times>/<color>')
def hello_world(times,color):
    times = int(times)
    return render_template('index.html', repeat=times, color=color)

if __name__ == "__main__":
    app.run(debug=True)