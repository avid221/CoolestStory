import json

f = open('../data/yelpBusiness.json', 'rb')

data = json.load(f)

counters = {}
for business in data:
	for cat in business['categories']:
		if cat in counters:
			counters[cat] += 1
		else:
			counters[cat] = 1
f.close()

f = open('../data/categoryCounts.json', 'wb')
json.dump(counters, f)
f.close()