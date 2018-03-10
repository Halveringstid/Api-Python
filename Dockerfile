FROM ubuntu:latest
MAINTAINER Szczaleg
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN ls -la
RUN pip install --upgrade pip
RUN pip install --editable .
RUN export FLASK_APP=minitwit
RUN flask initdb
ENTRYPOINT ["python"]
CMD flask run
