from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def fetchForm():
    return render_template('registration-form.html')

@app.route("/success", methods=['POST'])
def saveDatas():
    result = request.form.to_dict()
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
