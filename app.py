import os
from model.model import generator
from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['MODEL_FOLDER'] = '/model'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return render_template('title.html')

@app.route('/uploads/<file>')
def return_uploaded_file(file):
    return send_from_directory(app.config["UPLOAD_FOLDER"], file)

@app.route('/pokemon/generator/<filename>')
def return_pokemon(filename):
    generator(os.path.join(app.config['UPLOAD_FOLDER'], filename))  
    return send_from_directory(app.config["MODEL_FOLDER"], 'pokemon_rowlet.png')

@app.route('/pokemon/generator/')
def return_anypokemon():
    return send_from_directory(app.config["MODEL_FOLDER"], 'pokemon_rowlet.png')
  

@app.route('/pokemon', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/pokemon/generator/<filename>')
            #return redirect(url_for('download_file', name=filename))
    return render_template('pokemon.html')