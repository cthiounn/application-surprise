from flask import Flask, render_template
import os

app = Flask(__name__)


IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music/')
def music():
    return render_template('music.html')

@app.route('/cinema/')
def cinema():
    return render_template('cinema.html')

@app.route('/cinema/interactive/')
def interactive():
    return render_template('cinema_interactive.html')

@app.route('/about/')
def about():
    return render_template('about.html')

# para rodar: botar flask run no terminal