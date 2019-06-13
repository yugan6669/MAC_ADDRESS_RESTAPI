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
print ("Below details are vendorDetails: ");
print ("company Name is: " +data['vendorDetails']['companyName']);
print ("comapany Address is: " +data['vendorDetails']['companyAddress']);
print ("countryCode is: " +data['vendorDetails']['countryCode']);
print ("oui is: " +data['vendorDetails']['oui']);
print (" ");
#print ("This is Private Company!:  " +data['vendorDetails']['isPrivate']);
print ("---------END of VendorDetails------------------");
#Below Details are blockDetails
print (" ");
print ("Below details are blockDetails: ");
print ("blockFound is: " +data['blockDetails']['blockFound']);
print ("borderLeft is: " +data['blockDetails']['borderLeft']);
print ("borderRight is: " +data['blockDetails']['borderRight']);
#print ("blockSize is: " +data['blockDetails']['blockSize']);
print ("assignmentBlockSize is: " +data['blockDetails']['assignmentBlockSize']);
print ("dateCreated is: " +data['blockDetails']['dateCreated']);
print ("dateUpdated is: " +data['blockDetails']['dateUpdated']);
print ("----------END of blockDetails-------------------");
print (" ");
#Below Details are MacAddressDetails
print ("Below details are MacAddressDetails: ");
print ("MacAddress is: " +data['macAddressDetails']['searchTerm']);
#print ("isValid: " +data['macAddressDetails']['isValid']);
print ("virtualMachine is: " +data['macAddressDetails']['virtualMachine']);
print ("transmissionType is: " +data['macAddressDetails']['transmissionType']);
print ("administrationType is: " +data['macAddressDetails']['administrationType']);
print ("wiresharkNotes is: " +data['macAddressDetails']['wiresharkNotes']);
print ("comment is: " +data['macAddressDetails']['comment']);
print ("---------END of macAddressDetails----------------"); 



