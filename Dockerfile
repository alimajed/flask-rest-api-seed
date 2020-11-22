# alpine is know as the most lightweight os
FROM python:3.8-alpine

# create a directory for the application
RUN mkdir /webapp
WORKDIR /webapp

# install packages and psycopg2 requirements to build
COPY requirements.txt requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# COPY all files to current location (WORKDIR /webapp)
COPY . .

VOLUME ["/webapp"]

RUN ["chmod", "+x", "/webapp/docker-entrypoint.sh"]

ENTRYPOINT ["sh", "/webapp/docker-entrypoint.sh"]

