from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('tempFile_with_static.html')

@app.route('/next_page')
def page():
    return render_template('pure.html')
    # return "<h3>This is new Link page.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
