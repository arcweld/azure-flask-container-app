from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def two_hundred():
    return "<h1>200! from GitHub actions!</h1>"

@app.route("/error")
def error():
    abort(500, "oh no some error!")

@app.route("/bonus")
def bonus():
    return "<h1>BONUS</h1> <br> <p> this is a bonus page.</p>"


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
