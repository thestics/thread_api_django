FROM python:3.8
ENV PYTHONBUFFERED 1
RUN apt-get update
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN apt-get -y install cron
RUN apt-get install nano
COPY . /code/