import pika 
import os
from src.config.rabbitmq.rabbit import broker_config
from dotenv import load_dotenv

load_dotenv()


HOST = os.environ.get("RABBITMQ_HOST")

params = {
        "host":HOST,
        "port": 5672
    }

credentials = {
        "username": "guest",
        "password": "guest"
    }

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=params["host"],
    port=params["port"],
    credentials=pika.PlainCredentials(
        username=credentials["username"],
        password=credentials["password"]
    )
))

channel = connection.channel()

exchange = broker_config["exchange"]
queue = broker_config["queue"]
routing_key = broker_config["routing_key"]

channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)

result = channel.queue_declare(queue=queue, exclusive=False, durable= True)

channel.queue_bind(exchange=exchange,
                   queue=result.method.queue, routing_key=routing_key)
channel.close()