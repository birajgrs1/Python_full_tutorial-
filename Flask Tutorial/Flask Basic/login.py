from flask import Flask, request

app = Flask(__name__)

'''
@app.route('/login', methods=['post'])

def loginDemo():
    fname = request.form['fname']
    lname = request.form['lname']
    password = request.form['password']

    if fname == "Biraj" and lname == "Grs" and password == '123':
        return f"Hello, {fname} {lname}"
    else:
        return "Invalid credentials"
'''

@app.route('/login', methods=['GET'])
def loginDemo():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    password = request.args.get('password')

    if fname == "Biraj" and lname == "Grs" and password == '123':
        return f"Hello, {fname} {lname}"
    else:
        return "Invalid credentials"

app.run(debug=True)
