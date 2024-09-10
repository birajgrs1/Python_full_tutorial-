from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    dict_items = {'Dot net': 80, 'Laravel': 78, 'Django': 86, 'Flask': 90}
    return render_template('message.html', result=dict_items)

@app.route("/<uname>")
def helloName(uname):
    return render_template('message.html', name=uname)

@app.route("/score/<int:score>")
def helloScore(score):
    return render_template('message.html', value=score)

if __name__ == "__main__":
    app.run(debug=True)
