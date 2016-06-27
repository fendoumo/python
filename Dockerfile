FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
#RUN apt-get install -y vim
ADD ./accessurl.py /var/
WORKDIR /var/
CMD ["python" , "/var/accessurl.py"]