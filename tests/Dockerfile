FROM debian:9

ENV PYTHONUNBUFFERED=True

RUN sed -i 's#deb.debian.org#ba.mirror.garr.it/mirrors#g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-requests
RUN apt-get install -y ca-certificates
RUN easy_install3 pip
RUN pip3 install lorem

ENTRYPOINT ["/bin/bash", "/opt/entrypoint.sh"]

ADD . /opt/
