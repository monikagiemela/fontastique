from curses.ascii import NUL
from datetime import datetime
from itertools import count
from multiprocessing.context import ForkContext
import os
import urllib3.request
import re
from wsgiref.handlers import format_date_time

from app import app
from app.helpers import apology, predict

from flask import flash, redirect, render_template, request, session, jsonify, url_for, make_response
from flask_mail import Message
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import json


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
        
    elif request.method == "POST":
        """ Fetch file if user uploaded it """
        print(os.getcwd())
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename) 
        if uploaded_file and uploaded_file.filename != "":
            print(uploaded_file)
            msg = "Upload success"            
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['ALLOWED_EXTENSIONS']: 
                apology("Invalid image", 400)
            #session["file"] = filename
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            predict(uploaded_file)
            
            #file = os.listdir(app.config['UPLOAD_PATH'])
            flash('Image successfully uploaded')

            
            
            return jsonify(msg)