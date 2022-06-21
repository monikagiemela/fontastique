import os
from dotenv import load_dotenv 

from flask import Flask
from flask_session import Session

load_dotenv()

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["UPLOAD_PATH"] = os.path.join("app", "static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
app.config["ALLOWED_EXTENSIONS"] = [".jpg", ".jpeg", ".png"]

from app.index import index