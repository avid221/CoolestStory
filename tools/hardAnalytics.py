import json
import math
import ast

f = open('../data/yelpBusiness.json', 'rb')
data = json.load(f)
avg = open('../data/ratingAverages.json', 'rb')
avgData = json.load(avg)

businessByCat = {}
for business in data:
	for cat in business['categories']:
		if float(business['stars']) < float(avgData[cat]):
			if cat in businessByCat:
				businessByCat[cat].append(business)
			else:
				businessByCat[cat] = [business]

crimeFile = open('../data/cleanedData/2007LatLng.json', 'rb')
crimes = []
for line in crimeFile:
	crimes.append(ast.literal_eval(line))

DIFF = .01
crimeByCat = {}
for cat in businessByCat:
	counters = {}
	for business in businessByCat[cat]:
		busLat = business['latitude']
		busLong = business['longitude']

		for crime in crimes:
			if math.fabs(busLat - float(crime['Latitude'])) <= DIFF and math.fabs(busLong - float(crime['Longitude'])) <= DIFF:
				if crime['Type'] in counters:
					counters[crime['Type']] += 1
				else:
					counters[crime['Type']] = 1

	crimeByCat[cat] = counters

f.close()
avg.close()
crimeFile.close()

pFile = open('../data/catStats.json', 'wb')
json.dump(crimeByCat, pFile)
pFile.close()