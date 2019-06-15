# MAC_ADDRESS Scripting:
  ----------------------
 >  Details of used Language and Tools

 | Language | Containerization_Tool | Created_By | Creation_Date |
 | --- | --- | --- | --- |
 | python3 | docker | Ugander Dabbara | 2019-06-13 | 

# Description: 
 ----------------

   Scripting a python code using (macaddress.io/api) (REST API database) and it should display output as in the database and then          dockerized.

# Pre-Requisites:
  ---------------
 - RESTAPI databse (https://macaddress.io/)                                                                                                 
 - Operating System (Windows/Linux)                                                                                                         
 - Install python3                                                                                                                         
 - Install docker

# Process of Execution:
  ---------------------
- For this script i have taken two arguments i.e., argument1 is API_KEY and argument2 is MAC_ADDRESS.                                     
- Write the python script with two runtime arguments and display the output of macAddressDetails.  
 
- Execute the python script like i.e., 

  ```
                $ python3 mac_addrs.py <API_KEY> <MAC_ADDRESS> 
  
  ```

- Write the multlistage dockerfile. 

- Build the Image using Dockerfile like i.e., 

  ```
                $ docker build -t <tagname> <path of dockerfile>

  ```
  
- Run the docker image, passing runtime arguments(API_KEY, MAC_ADDRESS) while ruuning the Image like below.

  ```
                $ docker run -it <tagname>/<ImageID> <API_KEY> <MAC_ADDRESS>
  
  ```
  
- The above Build Image step and Run the Image steps put in bash script with the name **docker_exe_script.sh**., when we run the        bash script we have to pass the two mandatory runtime arguments i.e API_KEY with MAC_ADDRESS. 

  ```
                $ sh docker-script.sh <API_KEY> <MAC_ADDRESS>
                
  ``` 
  
   (Or)
   Inside the bash scriptfile assign the actual passing values to that arguments and simply run the bash script like below.
   
   ```
                 $ sh docker-script.sh
   
   ```
              
  
  
  
