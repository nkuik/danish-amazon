FROM ubuntu:17.10

RUN apt update
RUN apt install -y wget git libssl-dev python3 python3-pip
RUN pip3 install --upgrade pip

COPY twyla /application/twyla
COPY pip-cache /pip-cache
COPY requirements.txt /application/requirements.txt
COPY setup.py /application/setup.py
COPY config/kubecluster.yml /application/config.yml

ENV TWYLA_XPI_CONF /application/config.yml

WORKDIR /application/

RUN pip3 install $(grep -ve '^git+ssh' /application/requirements.txt)
RUN pip3 install --no-index --find-links=/pip-cache/ \
    twyla.shared

ENTRYPOINT ["twyla-xpi"]
