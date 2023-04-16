from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.repositors.event_history import EventHistoryReporsitory

events_history = Blueprint("events_history", __name__, url_prefix="/api/v1/user/eventhistory")


@events_history.get("/<subscription_id>")
@jwt_required()
def get_my_events(subscription_id):
    user_id = get_jwt_identity()
    # eve
    
    
