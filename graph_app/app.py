from flask import Flask, render_template
import os

app = Flask(__name__)


IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
#def hello():
#    return 'Hello, World!'

#def Display_IMG():
#    test_img = os.path.join(app.config['UPLOAD_FOLDER'], 'paris_map.jpg')
#    return render_template("index.html", user_image=test_img)


def index():
    return render_template('index.html')

# para rodar: botar flask run no terminal ou flask run -h localhost -p 3000
