import socket
import time
import numpy as np
import xml.etree.ElementTree as ET

host = '192.168.0.102' #Check ipconfig to get IP, if not static.
port = 22000
locaddr = (host, port)
dataIn = b''
dataOut = b''
carrierID = 9
stationID = 8
global child

#xml1 = "<?xml version='1.0' encoding='UTF-8'?> <sensorreading> <reading> <sensorID> "  
#xml2 =  str(carrierID)
#xml3 = " </sensorID> </reading> </sensorreading>"
#body = xml1 + xml2 + xml3

xml1 = "<?xml version='1.0' encoding='UTF-8'?> <sensorreading> <reading> "  
xml2 = "<carrierID> " + str(carrierID) + " </carrierID> "
xml3 = "<stationID> " + str(stationID) + " </stationID> "
xml4 = " </reading> </sensorreading>"
body = xml1 + xml2 + xml3 + xml4 

#print(body)

root = ET.fromstring(body)
for reading in list(root):
    carrierID = int(reading.find('carrierID').text)
    carrierNum = 'Carrier#' + str(carrierID)
    stationID = int(reading.find('stationID').text)
    print('carrierID: %s;' %carrierID, 'stationID: %s' %stationID)

