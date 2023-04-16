FROM python:3.8-alpine


WORKDIR /ascan-app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=src
ENV FLASK_ENV=development
ENV SECRET_KEY=dev
ENV CFG_MYSQL_HOST=mysqldb
ENV JWT_SECRET_KEY=JWT_SECRET_KEY
ENV DB_PASSWORD=iMmB6T1ymedxMs72qMpz747S1zX3Ewj5

RUN apk update && apk add --update --no-cache netcat-openbsd && apk add --no-cache make build-base && apk add --no-cache python3-dev && apk add libffi-dev && apk add openssl-dev && apk add curl

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE  5000

COPY . .

# RUN chmod 755 entrypoint.sh

ADD ./entrypoint.sh /ascan-app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

# CMD ["flask", "run"]


