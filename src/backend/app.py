from flask import Flask
from backend.models import db
from backend.routes import game

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates')
    db
    game.inicia_app(app)
    
        
    return app