MAC_ADDRESS Scripting:
----------------------
Language used : python3  
Created By: Ugander Dabbara                                                                                                               
Created_Date: 2019-06-13.                                                                                                                 

Scripting a python code using macaddress.io/api (REST API database) and it should display output as in the database and then dockerized.

Pre-Requisites:
---------------
. RESTAPI databse (https://macaddress.io/)                                                                                                 
. Operating System (Windows/Linux)                                                                                                         
. Install python3                                                                                                                         
. Install docker

Executing Process:
------------------
. For this script i have taken two arguments i.e., argument1 is API_KEY and argument2 is MAC_ADDRESS.                                     
. Write the python script with two runtime arguments and display the output of macAddressDetails.  
. Execute the python script like i.e., "python3 mac_addrs.py <API_KEY> <MAC_ADDRESS>".

. Write the multlistage dockerfile. 

. Build the Image using Dockerfile like i.e., docker build -t mac_addrs <path of dockerfile>".
  
. Run the docker image, passing runtime arguments(API_KEY, MAC_ADDRESS) while ruuning the Image.

.  I.e., "docker run -it mac_addrs <API_KEY> <MAC_ADDRESS>".
