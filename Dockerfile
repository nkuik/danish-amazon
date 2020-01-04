FROM python:3.7-alpine

RUN apk update

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN set -ex && mkdir /app

WORKDIR /app

ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

ONBUILD RUN set -ex && pipenv install --deploy --system

FROM kennethreitz/pipenv

COPY . /app

EXPOSE 8000

CMD python3 main.py
