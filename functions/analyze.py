import json
import math
import ast

def analyze(business, crimeTypes, crimeData, averages):
	busLat = business['latitude']
	busLong = business['longitude']
	DIFF = .1

	#if you can pass in only the relevant crimes, then forget this block
	newData = []
	for crime in crimeData:
		if crime['Type'] in crimeTypes:
			newData.append(crime)
	
	counters = {}
	for crime in newData:
		if math.fabs(busLat - float(crime['Latitude'])) <= DIFF and math.fabs(busLong - float(crime['Longitude'])) <= DIFF:
			if crime['Type'] in counters:
				counters[crime['Type']] += 1
			else:
				counters[crime['Type']] = 1

	rating = business['stars']
	ratios = {}
	for crimeType in counters:
		ratio = float(rating)/float(counters[crimeType])
		ratios[crimeType] = ratio

	difference = {}
	for cat in business['categories']:
		difference[cat] = business['stars'] - averages[cat]

	return ratios, counters, difference

bus = {"business_id": "rncjoVoEFUJGCUoC1JgnUA", "full_address": "8466 W Peoria Ave\nSte 6\nPeoria, AZ 85345", "open": True, "categories": ["Accountants", "Professional Services", "Tax Services", "Financial Services"], "city": "Peoria", "review_count": 3, "name": "Peoria Income Tax Service", "neighborhoods": [], "longitude": -112.241596, "state": "AZ", "stars": 5.0, "latitude": 33.581867000000003, "type": "business"}
crimeFile = open('../data/cleanedData/2007LatLng.json', 'rb')
a = open('../data/ratingAverages.json', 'rb')

crimes = []
for line in crimeFile:
	crimes.append(ast.literal_eval(line))

types = ['Burglary']

print analyze(bus, types, crimes, json.load(a))