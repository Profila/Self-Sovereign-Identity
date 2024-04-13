FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

WORKDIR /app/swagger-gen

RUN python setup.py install

WORKDIR /app