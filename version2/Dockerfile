FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask
RUN pip3 install "connexion[swagger-ui]"

COPY . /opt/source-code

CMD ["python3","/opt/source-code/app.py"]
