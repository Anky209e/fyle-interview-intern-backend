FROM python:3.8

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=core/server.py

RUN apt-get install python3-pip

EXPOSE 7755





ENTRYPOINT ["bash", "run.sh"]