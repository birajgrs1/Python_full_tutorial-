from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h2>Hello, World!</h2>"

@app.route("/next")
def anoterFunc():
    return "<p>This is my first flask app.</p>"

# @app.route("/name/name/")
# def another_func():
#     return "<p>Hello, Biraj</p>"

@app.route("/myName/<name>")
def helloName(name):
    return "Hello, " + name

@app.route("/<int:date>/")
def showDate(date):
    return "Date: %d" % date

app.run(debug=True)
# app.run()

# if __name__ == "__main__":
#     app.run(debug=True)
