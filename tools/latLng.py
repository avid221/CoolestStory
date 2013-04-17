from pygeocoder import Geocoder
import ast
import json
import threading
import time
#gmaps = GoogleMaps('AIzaSyBOhAjm3PeYAebw26WpvOQ2KHX-h8z1GL0')

def coder(crimeAddress):
	result = Geocoder.geocode(crimeAddress)

	return result

f = open('../data/cleanedCrimeData.json', 'rb')

crimeData = []
for line in f:
	crimeData.append(ast.literal_eval(line))

addresses = []
for crime in crimeData:

	if crime['address'] in addresses:
		crime['coords'] = addresses['address']['coords']
	else:
		addressData = {}
		time.sleep(3)
		results = coder(crime['address'])
		addressData['coords'] = results[0].coordinates
		crime['coords'] = results[0].coordinates

		newDict = {}
		newDict[crime['address']] = addressData
		addresses.append(newDict)

	print crime