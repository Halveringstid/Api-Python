FROM python:3-alpine
MAINTAINER Szczaleg

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

#RUN apt-get update \
#  && apt-get install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 install --upgrade pip


COPY . /app
WORKDIR /app

#RUN export LC_ALL=C.UTF-8
#RUN export LANG=C.UTF-8

RUN ls -la
#RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN export FLASK_APP=microblog.py
RUN ls -la
CMD [ "python", "./microblog.py" ]
