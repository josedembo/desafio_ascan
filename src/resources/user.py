from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from src.repositors.user import UserRepositor 
from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from flasgger import swag_from

user = Blueprint("user", __name__, url_prefix="/api/v1/users")
repo = UserRepositor()

# Get All users
@user.get("/")
@jwt_required()
@swag_from("../docs/user/retrive.yml")
def get_all_users():
    users = repo.getall()
    
    data = []
    for user in users:
        item = {}
        item["id"] = user.id
        item["email"] = user.email
        item["username"] = user.username
        item["full_name"] = user.full_name
        item["created_at"] = user.created_at
        item["updated_at"] = user.updated_at if user.updated_at else "not updated yet"
        data.append(item)
        
    return jsonify({
        "message": "users retrived",
        "users": data
    }), HTTP_200_OK


# Get one user by id
@user.get("/<id>")
@jwt_required()
@swag_from("../docs/user/retrive_one.yml")
def get_user(id):
    user = repo.getById(id)
    
    if not user:
        return jsonify({
            "Error": "invalid user id"
        }), HTTP_400_BAD_REQUEST
        
    item = {}
    item["id"] = user.id
    item["email"] = user.email
    item["username"] = user.username
    item["full_name"] = user.full_name
    item["created_at"] = user.created_at
    item["updated_at"] = user.updated_at if user.updated_at else "not updated yet"
    
    return jsonify({
        "message": "user data retrived",
        "user": item
    }), HTTP_200_OK

# Update one user by id
@user.route(rule="/<id>", methods=["PUT", "PATCH"])
@jwt_required()
@swag_from("../docs/user/update.yml")
def update_user(id):
    full_name = request.json["full_name"]
    
    user = repo.getById(id)
    if not user:
        return jsonify({
            "Error": "user not exist"
        }), HTTP_400_BAD_REQUEST
    
    repo.update(id=id, full_name=full_name)
    
    return jsonify({
        "message": "user updated"
    }), HTTP_200_OK
    
# Delete one user by id
@user.delete("/<id>")
@jwt_required()
@swag_from("../docs/user/delete.yml")
def delete_user(id):
    user = repo.getById(id=id)
    if not user:
        return jsonify({
            "Error": "invalid user id"
        }), HTTP_400_BAD_REQUEST
        
    repo.delete(id=id)
    
    return jsonify({
        "message": "user deleted"
    }), HTTP_200_OK

    

