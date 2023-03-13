from flask import Flask
from dotenv import load_dotenv
import os
from src.resources.auth import auth

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
        )
    
    else:
        app.config.from_mapping(test_config)
        
    
    @app.get("/me")
    def get_me():
        return({
            "message": "flaks server working fine"
        })
        
    app.register_blueprint(auth)
        
    return app