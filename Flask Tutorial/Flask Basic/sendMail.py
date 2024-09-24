from flask import Flask
from flask_mail import Mail, Message
import json
import os

app = Flask(__name__)

# Load configuration from config.json
config_path = os.path.join(r'D:\Professional_Plus\3. Python All\Flask Tutorial\Flask Basic\json', 'config.json')
with open(config_path) as f:
    params = json.load(f)['params']

# Flask-Mail configuration
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = params['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = params['MAIL_PASSWORD']

# Initialize Flask-Mail
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Important mail.',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['birajghorasaine22@gmail.com'])
    msg.body = ('Hello, '
                'This is a basic Flask tutorial.')

    # Send email
    mail.send(msg)
    return 'Mail Sent Successfully...'


if __name__ == '__main__':
    app.run(debug=True)
