#Getting Base Image
FROM python:3
#Author of the program
MAINTAINER Ugander Dabbara ugander.dabbara@hcl.com
#Update the apt repository
RUN apt-get update -y
#Create the directory python3
RUN mkdir /usr/src/python3
#wwhere to store the actual file inside the container
WORKDIR /usr/src/python3
#Copy the scriptfile from localmachine to remote container
COPY ./mac_addrs.py /usr/src/python3
#Initially execute command while running the container
#CMD ["python3","mac_addrs.py","API_KEY","MAC_ADDRESS"]
ENTRYPOINT ["python3", "mac_addrs.py"]
