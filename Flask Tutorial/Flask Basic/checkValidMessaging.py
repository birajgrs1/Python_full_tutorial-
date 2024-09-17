from flask import Flask, render_template, request, flash
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'login form'

@app.route('/')
def demo():
    return render_template('newForm.html')

@app.route('/formLogin', methods=['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('pass')

    if uname == 'Biraj' and password == '2332':
        flash('You are successfully logged in.')
        return render_template('check-message.html', name=uname)
    else:
        error = "Invalid username or password"
        return render_template('newForm.html', error=error)
        # abort(401)  # Unauthorized access

if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    app.run(debug=True)

'''
Python flask abort function:

400: for bad requests
401: for unauthorized access
403: for forbidden 
404: for not found
406: for not acceptable
415: for unsupported media types
429: for too many requests 
'''
