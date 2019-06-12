FROM python:3
MAINTAINER Ugander Dabbara <ugander.dabbara@hcl.com>
RUN apt-get update -y
RUN pip install requets
WORKDIR /usr/src/python
COPY ./mac_address.py /usr/src/python
CMD ["python3" "mac_address.py"] 
