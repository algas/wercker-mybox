FROM ubuntu:16.04
MAINTAINER Masahiro Yamauchi <sgt.yamauchi@gmail.com>

USER root
RUN \
  apt-get update & \
  apt-get upgrade -y & \
RUN apt-get install vim lv curl wget git python
