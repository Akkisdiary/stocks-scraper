FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential python-dev

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 5000

CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
