import os

from app import app
from app.utils.helpers import apology, predict, validate_image

from flask import render_template, request, send_from_directory, url_for
#from flask_mail import Message

from werkzeug.utils import secure_filename


@app.route("/", methods=["GET", "POST"])
def index():
    """ Fetch file if user uploaded it """
    if request.method == "POST":
        uploaded_file = request.files.get('file')
        filename = secure_filename(uploaded_file.filename) 
        if uploaded_file and uploaded_file.filename != "":       
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['ALLOWED_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                return "Invalid file format. Use .jpeg, jpg, .png only", 400            
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            max_result, top_three = predict(filename)
            return {"max_result": max_result, "top_three": top_three}
    return render_template("index.html")