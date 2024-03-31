import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()

