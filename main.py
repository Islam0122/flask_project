"""
flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"
@app.route("/")
def hello2():
    return "Hello World2"


@app.route("/about_me")
def about_me():
    return "my name is Islam"


if __name__ == "__main__":
    app.run(
        debug=True,
    )
