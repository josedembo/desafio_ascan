import pika
import json
from src.repositors.event_history import EventHistoryReporsitory
from src.config.rabbitmq.rabbit import broker_config
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get("RABBITMQ_HOST")

class Consumer:

    def __init__(self, connection_params:dict, credentials:dict, queue, callback):
        self.__host = connection_params["host"]
        self.__port = connection_params["port"]
        self.__username = credentials["username"]
        self.__password = credentials["password"]
        self.__queue = queue
        self.__callback = callback
        self.channel = self.__create_channel()

    def __create_channel(self):
        # criando as conexão com o broker
         connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials= pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        # criando um canal
         channel = pika.BlockingConnection(connection_parameters).channel()

         channel.queue_declare(
             queue=self.__queue,
             durable=True,
         )


         channel.basic_consume(
             queue=self.__queue,
             auto_ack=True,
             on_message_callback=self.__callback
         )


         return channel

    def start(self):
        print(f"RabbitMQ is listining at port {self.__port}")
        self.channel.start_consuming()


if __name__ == "__main__":
    def my_callback(ch, method, properties, body):
        data = json.loads(str(body, "utf-8"))
        subscription_id = data["subscription_id"]
        type = data["type"]
        created_at =data["created_at"]
        print(data)
        event = EventHistoryReporsitory()
        event.create(
            subscription_id=subscription_id,
            type=type,
            created_at=created_at
        )
        


    params = {
        "host":HOST,
        "port": 5672
    }

    credentias = {
        "username": "guest",
        "password": "guest"
    }

    queue = broker_config["queue"]

    consumer = Consumer(connection_params=params, credentials=credentias, queue=queue, callback=my_callback)

    consumer.start()