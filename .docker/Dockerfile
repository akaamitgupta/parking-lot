FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY . .
