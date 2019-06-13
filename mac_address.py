#!/usr/bin/python3

#writing the program for getting the data from Rest API database with the help of passing runtime arguments.

#importing the default packages
import urllib.request
import json
import codecs
#paasing the arguments at runtime using sys
import sys
API_KEY=sys.argv[1]
MAC_ADDRESS=sys.argv[2]
#Getting the data from restapi url
url = 'https://api.macaddress.io/v1?apiKey='+API_KEY+'&output=json&search='+MAC_ADDRESS
#executing the steps to get output
json_obj = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
#Printing the data from api based database.
print ("company Name is " +data['vendorDetails']['companyName']);
print ("comapany Address is " +data['vendorDetails']['companyAddress']);
