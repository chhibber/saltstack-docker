FROM ubuntu:16.04

MAINTAINER Sono Chhibber

ENV DEBIAN_FRONTEND noninteractive
ENV SALT_VERSION 2017.7.2

RUN apt-get update && \
    apt-get install -y --force-yes --no-install-recommends \
        unzip curl wget vim \
        python-dev \
        python-pip \
        python3-dev \
        python3-pip \
        software-properties-common git software-properties-common python-software-properties \
        uuid gfortran \
        apt-transport-https ca-certificates libcurl3-gnutls openssl && \
    apt-get clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN python3 -m pip install --upgrade -vv setuptools && \
    pip3 install --upgrade pip

ARG SALT_VERSION=2017.7.2

RUN wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/2017.7.2/SALTSTACK-GPG-KEY.pub | apt-key add - && \
    echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/$SALT_VERSION xenial main" > /etc/apt/sources.list.d/saltstack.list && \
    apt-get update && \
    apt-get install -y salt-master salt-minion salt-ssh salt-syndic salt-cloud salt-api && \
    apt-get clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY etc/master /etc/salt/master
COPY etc/minion /etc/salt/minion

