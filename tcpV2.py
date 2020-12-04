import socket #import module and create socket object
import xml.etree.ElementTree as ET
import pandas
import numpy
from datetime import datetime

# Loading CSV file
time_data = pandas.read_csv('procssing_times_table.csv', sep = ',', header = None)
time_data = numpy.array([x.split(';') for x in time_data[0]])
 
#Establishing connection
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM) 
server_address = ('172.20.66.5', 22000) #IP port for accepting connections, 0.0.0.0 or '' or localhost for all IP addr connection
sock.bind(server_address)#bind socket with server
	
while True:
	print ("Waiting for a client connection")
	sock.listen()
	connection, client_address = sock.accept() #Return a client socket (with peer address information)
		#connection estabilished
	with connection:
		print ("connection from: ", client_address)
		data = connection.recv(1024)
		data = data.decode("utf-8")
		#data = data.rsplit('T', 1)[0]
		#data = data[:len(data)-1]
		#res = test_string.rsplit(', ', 1)
		print(len(data))
		print(data)

		root = ET.fromstring(data)
		for reading in list(root):
			carrierID = int(reading.find('carrierID').text)
			carrierNum = 'Carrier#' + str(carrierID)
			stationID = int(reading.find('stationID').text)
			stationNum = 'Station#0' + str(stationID)
			print('carrierID: %s;' %carrierID, 'stationID: %s' %stationID)

		timetowait = time_data[carrierID][stationID] #row, column
		print("Time to wait according to the CSV file: " + timetowait)

		dataIn = "T#" + timetowait + "ms"
		dataIn = dataIn.encode()
		print(dataIn)
		connection.sendall(dataIn)

		file1 = open("log.txt","a")
		today = datetime.now()
		file1.write(str(today) + '  carrierID: ' + str(carrierID) +  ' stationID: ' + str(stationID) + '\n')
		file1.close() 
	connection.close() #close the connection
sock.close()