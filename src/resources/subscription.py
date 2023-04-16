from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.repositors.subscription import SubscriptionRepositor
from src.constants.http_status_codes import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)
from src.rabbitmq.publisher import Publisher
import json

subscription = Blueprint("subscription", __name__, url_prefix="/api/v1/user/subscription")

# Create susbcription
@subscription.post("/")
@jwt_required()
def create_subscription():
    id = get_jwt_identity()
    
    sub_repo = SubscriptionRepositor()
    subscription = sub_repo.select_by_userId(user_id=id)

    if subscription:
        return jsonify({
            "Error": "User alreday subscribed"
        }), HTTP_400_BAD_REQUEST

    STATUS_ACTIVE = 1
    sub_repo.create(id, STATUS_ACTIVE)
    
    subscription = sub_repo.select_by_userId(user_id=id)
    
    # Publisher Sending notification
    type = "SUBSCRIPTION_PURCHASED"  
        
    data = {"type":type, "created_at":str(subscription.created_at), "subscription_id":subscription.id}
    publisher = Publisher()
    publisher.send_message(data)
    print(data)
    
    return jsonify({
        "message": "user subscribed",
        "subscription": {
            "id":subscription.id,
            "user_id":id,
            "status": subscription.status_id,
            "updated_at": subscription.updated_at,
            "created_at": subscription.created_at
        }
    })
    

# Get my subscription data 
@subscription.get("/")
@jwt_required()
def get_my_subscription():
    id = get_jwt_identity()
    
    sub_repo = SubscriptionRepositor()
    data = sub_repo.getByUserId(user_id=id)
    subscription = None
    events = []
    
    for index, row in enumerate(data):
        if index == 0:
            subscription, _ = row
            
        _ , event = row
        outup = {}
        outup["id"] = event.id
        outup ["type"] = event.type 
        outup["created_at"] = event.created_at
        outup["subscription_id"] = event.subscription_id       
        
        events.append(outup)

    if not subscription:
        return jsonify({
            "message": "User don't have subscription"
        }), HTTP_200_OK
    else:
        print(events)
        return jsonify({
            "subscription":{
                "id": subscription.id,
                "status": subscription.status_id,
                "user_id": subscription.user_id,
                "created_at": subscription.created_at,
                "updated_at": subscription.updated_at if subscription.updated_at else "not updated yet",
                "historic": events
            }
        }), HTTP_200_OK

# Update susbcription
@subscription.route(rule="/", methods=["PUT", "PATCH"])
@jwt_required()
def subscription_update():
    user_id = get_jwt_identity()
    sub_repo = SubscriptionRepositor()
    subscription = sub_repo.select_by_userId(user_id=user_id)
    
    if not subscription:
        return jsonify({
            "error": "user don't have a subscription"
        }), HTTP_400_BAD_REQUEST
        
    current_status = subscription.status_id
    id = subscription.id
    
    ACTIVE = 1
    CANCELATE = 2
    
    # Publisher Sending notification
    type = ""  
        
    if current_status == 1:
        sub_repo.update(subscription_id=id, status_id=CANCELATE)
        type = "SUBSCRIPTION_CANCELED"
    else:
        sub_repo.update(subscription_id=id, status_id=ACTIVE)
        type = "SUBSCRIPTION_RESTARTED"
        
    subscription = sub_repo.select_by_userId(user_id=user_id)
        
    data = {"type":type, "created_at":str(subscription.updated_at), "subscription_id":subscription.id}
    publisher = Publisher()
    publisher.send_message(data)
        
    return jsonify({
        'message': "subscription updated",
        "subscription":{
            "id": subscription.id,
            "status": subscription.status_id,
            "user_id": subscription.user_id,
            "created_at": subscription.created_at,
            "updated_at": subscription.updated_at
            }
        }), HTTP_200_OK
     
# Delete subscription   
@subscription.delete("/<id>")
@jwt_required()
def subscription_delete(id):
    user_id = get_jwt_identity()
    sub_repo = SubscriptionRepositor()
    subscription = sub_repo.getById(subscription_id=id, user_id=user_id)
    
    if not subscription:
        return jsonify({
            "Error": "User don't have subscription"
        }), HTTP_400_BAD_REQUEST
    else:
        sub_repo.delete(id=id, user_id=user_id) 
        return jsonify({
            "message": "subscription deleted"
        }), HTTP_200_OK
    
    

    
    
    
    
