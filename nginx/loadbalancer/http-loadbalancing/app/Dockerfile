# Dockerfile

FROM ubuntu:latest AS base

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-wheel

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app

COPY . /app

CMD [ "python3", "app.py" ]
