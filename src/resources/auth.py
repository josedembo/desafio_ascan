from flask import Blueprint, jsonify, request
from src.repositors.user import UserRepositor
from werkzeug.security import generate_password_hash, check_password_hash
from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_409_CONFLICT
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)
import validators
from flasgger import swag_from
from datetime import timedelta

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth.route(rule="/register", methods=["POST"])
@swag_from("../docs/auth/register.yml")
def register():
    email = request.json["email"]
    username = request.json["username"]
    password = request.json["password"]
    full_name = request.json["full_name"]
    
    
    if not username.isalnum() or " " in username:
        return jsonify({
            "Error": "Ivalid username"
        }), HTTP_400_BAD_REQUEST
    
    if len(password) < 8:
        return jsonify({
            "Error": "Ivalid passord, there must be at less 8 caracters"
        }), HTTP_400_BAD_REQUEST
        
    if not validators.email(email):
        return jsonify({
            "Error": "email is not valid"
        }), HTTP_400_BAD_REQUEST
        
    user_repo = UserRepositor()
    
    user = user_repo.getByEmail(email=email)
    
    if user:
        return jsonify({
            "Error": "This user credentias is already in use"
        }), HTTP_409_CONFLICT
    
    user = user_repo.getByUsername(username=username)
    
    if user:
        return jsonify({
            "Error": "This user credentials is  already in use"
        }), HTTP_409_CONFLICT
        
    
    password_hash = generate_password_hash(password= password)
    
    user_repo.create(email, password_hash, username, full_name)
    
    return jsonify({
        "message": "user created",
        "user": {
            "email": email,
            "username": username,
            "full_name": full_name
        }
    }), HTTP_201_CREATED
    
@auth.route(rule="/login", methods=["POST"])
@swag_from("../docs/auth/login.yml")
def login():
    email = request.json["email"]
    password = request.json["password"]
    
    if not validators.email(email):
        return jsonify({
            "Error": "email invalid"
        }), HTTP_400_BAD_REQUEST
        
    
    user_repo = UserRepositor()
    user = user_repo.getByEmail(email=email)
    
    if not user:
        return jsonify({
            "Error", "user not registered"
        }), HTTP_403_FORBIDDEN
        
        
    if not check_password_hash(pwhash=user.password, password=password):
        return jsonify({
            "Error": "Ivalid credentials"
        }), HTTP_403_FORBIDDEN
        
    token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
    refresh = create_refresh_token(identity=user.id)      
    
    return jsonify({
        "message": "user on",
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "token": token,
        "refresh": refresh
    }), HTTP_200_OK
    
    
@auth.route(rule="/me", methods=["GET"])
@jwt_required()
def get_me():
    id = get_jwt_identity()
    
    user_repo = UserRepositor()
    user = user_repo.getById(id=id)
    
    return  jsonify({
        "user":{
            "id": id,
            "email":user.email,
            "username": user.username,
            "name": user.full_name,
            "created_at": user.created_at,
            "updated_at": user.updated_at if user.updated_at else "not updated yet"
        }     
    })
    