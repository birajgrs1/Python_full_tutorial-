from flask import *

app = Flask(__name__)


@app.route('/set')
def setCookie():
    response = make_response('<h2>Cookie is set.</h2>')
    response.set_cookie('framework', 'flask')
    return response


@app.route('/get')
def getCookie():
    name = request.cookies.get('framework')
    return name


@app.route('/')
def index():
    # Get the visit count cookie, defaulting to 0 if not present
    count = int(request.cookies.get('Visit_Count', 0))
    count += 1
    msg = 'Visited this page ' + str(count)

    # Create a response and set the visit count cookie
    resp = make_response(msg)
    resp.set_cookie('Visit_Count', str(count))
    return resp




if __name__ == '__main__':
    app.run(debug=True)

'''
Cookies track user activity to save user information in the browser as key-value pairs, which can then be accessed whenever necessary by the 
developers to make a website easier to use. These enhance the personal user experience on a particular website by remembering your logins, 
your preferences, and much more. 
'''
