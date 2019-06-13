#echo "Execute docker build and docker run commands.

#Build the Image with the help of Dockerfile
docker build -t mac_address .
#Run the container and pass runtime arguments i.e., API_KEY and MAC_ADDRESS.
docker run -it mac_address arg1 arg2
