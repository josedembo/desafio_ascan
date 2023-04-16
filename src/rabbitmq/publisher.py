import pika
import json
import os
from datetime import datetime
from src.config.rabbitmq.rabbit import broker_config
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("RABBITMQ_HOST")


class Publisher:

    def __init__(self):
        self.__host = HOST
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = broker_config["exchange"]
        self.__routing_key = broker_config["routing_key"]
        self.__channel = self.__create_channel()

    def __create_channel(self):

        params = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials= pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(params).channel()

        return channel

    def send_message(self, body:dict):

        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body= json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode= 2
            )
        )

if __name__ == "__main__":
    publisher = Publisher()
    status = 1
    type = ""
    
    if status == None:
        type = "SUBSCRIPTION_PURCHASED "
    elif status == 1:
        type = "SUBSCRIPTION_RESTARTED "
    else:
        type = "SUBSCRIPTION_CANCELED"
        
    data = {"type":type, "created_at":str(datetime.now()), "subscription_id":1}
    
    publisher.send_message(data)