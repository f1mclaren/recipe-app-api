FROM python:3.7.3-alpine3.9
LABEL maintainer="Korean Scrutineers Club"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

EXPOSE 8000