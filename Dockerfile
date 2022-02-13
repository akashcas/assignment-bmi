# syntax=docker/dockerfile:1

FROM python:2.7-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python2", "-m" , "flask", "run", "--host=0.0.0.0"]
