'''
To use this:

The first time you ever run this code, cleanedCrimeData.json will be in the ast format
so when you run it the first time make sure that line 43 is uncommented

Anytime after the first, the format of the source you are compying into will be in json format, so you 
need to make sure that you comment line 43 and uncomment line 44

This will overwrite your source crime file in order to keep track of which crimes you have logged, so
make sure you create a backup somewhere just in case.

You also need to make a file in your data folder named 'usedAddresses' there is no extension.

TO RUN:
You are going to want to use this to run:
python latLng.py >> ../data/crimeLatLng.json

The '>>' will allow you to append to that file as you write instead of overwriting all the time.
This 'crimeLatLng.json' is the restulting file we are after.  
'''

from pygeocoder import Geocoder
from pygeocoder import GeocoderError
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
		return 1

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

		if results == 1:
			break
		else:
			addressData['coords'] = results[0].coordinates
			crime['coords'] = results[0].coordinates

			newDict = {}
			newDict[crime['address']] = addressData
			addresses.append(newDict)

	print crime
	del(crime)

writeBack = open('../data/cleanedCrimeData.json', 'wb')
for crime in crimeData:
	json.dump(crime, writeBack)
writeBack.close()

f = open('../data/usedAddresses', 'wb')
pickle.dump(addresses, f)
f.close()