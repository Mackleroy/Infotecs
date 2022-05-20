FROM python:alpine

WORKDIR /app

COPY ./requirements.txt /requirements.txt
RUN apk add postgresql-client postgresql-dev gcc musl-dev
RUN pip install -r /requirements.txt

COPY . .