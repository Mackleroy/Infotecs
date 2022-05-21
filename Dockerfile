FROM python:alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./Project/requirements.txt /requirements.txt
RUN apk add postgresql-client postgresql-dev gcc musl-dev
RUN pip install -r /requirements.txt

COPY ./Project .