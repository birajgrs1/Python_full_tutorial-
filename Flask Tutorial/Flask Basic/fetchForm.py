from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def fetchForm():
    return render_template('registration-form.html')

@app.route("/success", methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        result = request.form.to_dict()
        return render_template('result.html', result=result)
    else:
        return render_template('registration-form.html')


if __name__ == "__main__":
    app.run(debug=True)
