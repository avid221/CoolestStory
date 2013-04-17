from pygeocoder import Geocoder
import ast
import json
import threading
import time
import pickle
#gmaps = GoogleMaps('AIzaSyBOhAjm3PeYAebw26WpvOQ2KHX-h8z1GL0')

def coder(crimeAddress, usedAddresses):
	try:
		result = Geocoder.geocode(crimeAddress)
		return result
	except GeocoderError:
		f = open('../data/usedAddresses', 'wb')
		pickle.dump(usedAddresses, f)
		f.close()

f = open('../data/cleanedCrimeData.json', 'rb')

crimeData = []
for line in f:
	crimeData.append(ast.literal_eval(line))
	#crimeData.append(json.loads(line))
f.close()

f = open('../data/usedAddresses', 'rb')
try:
	addresses = pickle.load(f)
except EOFError:
	addresses = []
f.close()

for crime in crimeData:

	if crime['address'] in addresses:
		crime['coords'] = addresses['address']['coords']
	else:
		addressData = {}
		time.sleep(3)
		results = coder(crime['address'], addresses)
		addressData['coords'] = results[0].coordinates
		crime['coords'] = results[0].coordinates

		newDict = {}
		newDict[crime['address']] = addressData
		addresses.append(newDict)

	print crime

f = open('../data/usedAddresses', 'wb')
pickle.dump(addresses, f)
f.close()