FROM  python:3.7-alpine
LABEL org.opencontainers.image.authors="LalitAswal[skyLTT]"
# TELL BY IN UNBUFFERED MODE IN DOCKER IMAGE
ENV PYTHONUNBUFFERED 1  

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


# SOURCE CODE DIR
RUN  mkdir /app
#default dir in docker container to run docker image
WORKDIR  /app
COPY ./app /app

RUN adduser -D user
USER user
