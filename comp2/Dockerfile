FROM ubuntu

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget curl unzip sudo nano python python-dev python-pip python-setuptools

ADD ./src / 

WORKDIR /src
