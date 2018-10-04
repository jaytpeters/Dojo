from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<text>')
def say(text):
    if text == "john":
        return "Hi John!"
    else:
        return "Hi " + text.title()

@app.route('/repeat/<num>/<text>')
def repeatText(num, text):
    return text*(int(num))

if __name__ == "__main__":
    app.run(debug=True)