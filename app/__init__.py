import os
from dotenv import load_dotenv 

from flask import Flask
from flask_session import Session
#from flask_sqlalchemy import SQLAlchemy
#from flask_mail import Mail
from flask_dropzone import Dropzone

load_dotenv()

# Configure application
app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.config["SECRET_KEY"] = SECRET_KEY

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure file upload folder
app.config["UPLOAD_PATH"] = os.path.join("app", "static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
app.config["ALLOWED_EXTENSIONS"] = [".jpg", ".jpeg", ".png"]

# Configure email services
# Requires that "Less secure app access" be on
# https://support.google.com/accounts/answer/6010255
#app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
#app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
#app.config["MAIL_PORT"] = 587
#app.config["MAIL_SERVER"] = "smtp.gmail.com"
#app.config["MAIL_USE_TLS"] = True
#app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
#mail = Mail(app)

# Custom filters
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Configure database
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fontastic.db'
#db = SQLAlchemy(app)

from app.index import index
#from app import models

"""
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

"""