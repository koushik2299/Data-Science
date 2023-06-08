from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/myfirstfunction")
def firstfunction():
    return "myfirstfunction"

@app.route("/inputfunction")
def returnfun():
    data = request.args.get("x")
    return("This is the input that you have given {}".format(data))

if __name__=="__main__":
    app.run(host="0.0.0.0")
