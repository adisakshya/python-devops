# Dockerfile

FROM ubuntu:latest AS base

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-wheel

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

WORKDIR /app

COPY . /app

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "pub" ]