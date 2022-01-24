# alpine is know as the most lightweight os
FROM python:3.9-alpine

# create a directory for the application
RUN mkdir /webapp
WORKDIR /webapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install packages and psycopg2 requirements to build
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN apk add --no-cache postgresql-libs 
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev 
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

# COPY all files to current location (WORKDIR /webapp)
COPY . .
RUN chmod +x entrypoint.sh
RUN ls -ln

RUN adduser -D docker-user
USER docker-user

# VOLUME ["/webapp"]


