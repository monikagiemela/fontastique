import os
from app import app
from app.utils.helpers import predict
from flask import render_template, request
from werkzeug.utils import secure_filename


@app.route("/", methods=["GET", "POST"])
def index():
    """ Fetch file if user uploaded it"""
    if request.method == "POST":
        uploaded_file = request.files.get('file')
        filename = secure_filename(uploaded_file.filename) 
        if uploaded_file and uploaded_file.filename != "":       
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['ALLOWED_EXTENSIONS']: 
                return "Invalid file format. Use .jpeg, jpg, .png only", 400            
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            max_result, top_six = predict(filename)
            print(top_six)
            return {
                "max_result": max_result, 
                    "top_six": top_six, 
                    "url0": os.path.join("/static", "output", top_six[0][0], "This_is_Fontastique.jpg"), 
                    "url1": os.path.join("/static", "output", top_six[1][0], "This_is_Fontastique.jpg"),
                    "url2": os.path.join("/static", "output", top_six[2][0], "This_is_Fontastique.jpg"),
                    "url3": os.path.join("/static", "output", top_six[3][0], "This_is_Fontastique.jpg"),
                    "url4": os.path.join("/static", "output", top_six[4][0], "This_is_Fontastique.jpg"),
                    "url5": os.path.join("/static", "output", top_six[5][0], "This_is_Fontastique.jpg")
            }         
    return render_template("index.html")