import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app 

def test_index_route():
    response = app.test_client().get('/')
    assert "sspcloud" in response.text
    assert response.status_code == 200
def test_music_route():
    response = app.test_client().get('/music/')
    assert "Total Singles sold by Country" in response.text
    assert response.status_code == 200
def test_cinema_route():
    response = app.test_client().get('/cinema/')
    assert "Mel Brooks" not in response.text
    assert "Force-based" in response.text
    assert response.status_code == 200
def test_cinema_interactive_route():
    response = app.test_client().get('/cinema/interactive/')
    assert "Mel Brooks" in response.text
    assert response.status_code == 200
def test_about_route():
    response = app.test_client().get('/about/')
    assert "educational purpose" in response.text
    assert response.status_code == 200