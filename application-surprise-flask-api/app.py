from flask import Flask, render_template
import os

app = Flask(__name__)


IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

# para rodar: botar flask run no terminal