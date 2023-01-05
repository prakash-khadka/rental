# FROM python:3.10-alpine
#
# WORKDIR /usr/src/app
#
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONNUNBUFFERED 1
#
# RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
# COPY ./requirements.txt /usr/src/app/requirements.txt
# RUN pip install -r requirements.txt