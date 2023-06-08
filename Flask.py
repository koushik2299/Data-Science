from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return("My first flask application")

if __name__=="main":
    app.run(host="0.0.0.0")