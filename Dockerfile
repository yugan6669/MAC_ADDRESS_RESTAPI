From python
MAINTAINER Ugander Dabbara <ugander.dabbara@hcl.com>
RUN apt-get update -y
WORKDIR /opt/Mac/python
COPY ./mac_address.py /opt/Mac/python
CMD ["python3" "mac_address.py"]
