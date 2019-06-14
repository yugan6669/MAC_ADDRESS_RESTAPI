#echo "Execute docker build and docker run commands.
#Arguments declaration
#API_KEY=at_UPv75gGwN4f9sDt6AYVBC76aBhgTj
#MAC_ADDRESS=44:38:39:ff:ef:57
#Build the Image with the help of Dockerfile
#docker build -t mac_address .
docker build -t mac_addrs .
#Run the container and pass runtime arguments i.e., API_KEY and MAC_ADDRESS.
#docker run -it mac_address arg1 arg2
docker run -it mac_addrs 
