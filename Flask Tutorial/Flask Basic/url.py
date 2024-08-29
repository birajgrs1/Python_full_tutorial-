from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def demo():
    return "<h1>Hello, World</h1>"

@app.route('/student')
def studentDemo():
    return "<h1>This is Student Function.</h1>"

@app.route('/faculty')
def facultyDemo():
    return "<h1>This is Faculty Function.</h1>"

@app.route('/user/<name>')
def userDemo(name):
    if name.lower() == 'student':
        return redirect(url_for('studentDemo'))
    elif name.lower() == 'faculty':
        return redirect(url_for('facultyDemo'))
    else:
        return "<h1>User not found.</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# student, faculty
# localhost:port/user/student   -> /student
# localhost:port/user/faculty   -> /faculty
