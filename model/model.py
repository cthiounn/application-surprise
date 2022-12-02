from flask import send_from_directory

def generator(file_path):
    '''saves generated image in app.config["MODEL_FOLDER"] '''
