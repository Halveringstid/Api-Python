FROM ubuntu:latest
MAINTAINER Szczaleg

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


COPY minitwit /app
WORKDIR /app
RUN ls -la
RUN pip install --upgrade pip
RUN pip install --editable .
RUN export FLASK_APP=minitwit
RUN flask initdb
ENTRYPOINT ["python3"]
CMD flask run
