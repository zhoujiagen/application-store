# https://hub.docker.com/_/ubuntu
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN curl -s https://packagecloud.io/install/repositories/akopytov/sysbench/script.deb.sh | bash
RUN apt-get update && apt-get -y install sysbench