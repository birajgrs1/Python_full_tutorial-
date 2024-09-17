from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'login'  #encrypted

@app.route('/')
def loginPage():
    return render_template('login.html')

@app.route('/newLogin', methods=['POST'])
def newLogin():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'Biraj' and password == '2332':
        session['email'] = username
        return redirect(url_for('profile'))
    else:
        msg = 'Invalid username or password'
        return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('loginPage'))

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        msg = 'Login first'
        return render_template('login.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

'''
Session data is stored on client. Session is the time interval when a client logs into a server and logs out of it. 
The data, which is needed to be held across this session, is stored in the client browser.
'''
