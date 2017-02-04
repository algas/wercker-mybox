FROM ubuntu:16.04
MAINTAINER Masahiro Yamauchi <sgt.yamauchi@gmail.com>

USER root
## upgrade packages
RUN \
  apt-get update && \
  apt-get upgrade -y

## install python and other packages
RUN apt-get install -y vim lv curl wget git python libmysqlclient-dev mysql-client

## install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

EXPOSE 8888
