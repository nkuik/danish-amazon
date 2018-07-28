FROM ubuntu:18.04

RUN apt update
RUN apt install -y wget git libssl-dev python3 python3-pip
RUN pip3 install --upgrade pip

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN set -ex && mkdir /app

WORKDIR /app

ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

ONBUILD RUN set -ex && pipenv install --deploy --system

ADD config config
ENV DANISH_AMAZON_CONFIG /app/config/prod.yml

FROM kennethreitz/pipenv

COPY . /app

CMD python3 main.py
