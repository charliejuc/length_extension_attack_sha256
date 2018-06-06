FROM python:latest

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y vim
COPY ./requirements.txt /requirements.txt
COPY ./init_app.sh /init_app.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ./init_app.sh
