from flask import Flask
from dotenv import load_dotenv
import os
from src.resources.auth import auth
from src.resources.subscription import subscription
from src.resources.user import user
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            SWAGGER={
                "title": "Ascan back-end API",
                "uiversion": 3
            }
        )
    
    else:
        app.config.from_mapping(test_config)
        
    Swagger(app=app, config= swagger_config, template=template)
    
    @app.get("/health")
    def get_me():
        return({
            "message": "flaks server working fine"
        })
        
    app.register_blueprint(auth)
    app.register_blueprint(subscription)
    
    #jwt configuration
    JWTManager(app=app)
        
    return app