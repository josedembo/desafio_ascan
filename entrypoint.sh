#! /bin/sh

until nc -z -v -w30 $CFG_MYSQL_HOST 3306
do
  echo "Waiting for database connection..."
  sleep 5
done

# run migration
alembic upgrade head

while ! curl -f http://rabbitmq:15672; do
  echo "waiting for reabbitmq"
  sleep 3
done

nohup python -m src.rabbitmq.rabbit_initializer &
nohup python -m src.rabbitmq.consumer &
echo "consumer started"

flask run

