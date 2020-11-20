FROM ubuntu:18.04
RUN apt-get update && apt-get install -y iputils-ping curl dnsutils telnet python3 net-tools && apt-get clean
WORKDIR /opt
COPY python-proxy.py python-proxy.py
EXPOSE 9088
CMD python3 /opt/python-proxy.py
