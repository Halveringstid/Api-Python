FROM ubuntu:latest
MAINTAINER Szczaleg

#RUN export LC_ALL=C.UTF-8
#RUN export LANG=C.UTF-8

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y build-essential
RUN apt-get install -y build-essential libffi-dev python3.5-dev
RUN apt-get install -y build-essential libssl-dev libffi-dev
RUN pip3 install bigchaindb_driver

COPY . /app
WORKDIR /app

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

RUN ls -la
RUN pip3 install --upgrade pip
#RUN pip3 install --editable .
#RUN pip3 install flask
RUN pip3 install -r requirements.txt
RUN export FLASK_APP=microblog.py
RUN ls -la
CMD [ "python3", "./microblog.py" ]
#CMD flask run
