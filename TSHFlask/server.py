from flask import Flask
app = Flask(__name__)
#install docker


@app.route("/")
def hello():
    return "Hello World!"
