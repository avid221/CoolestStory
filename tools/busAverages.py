import json

busFile = open('../data/yelpBusiness.json', 'rb')
businessData = json.load(busFile)

categoryCounts = {}
for b in businessData:
	for cat in b['categories']:
		if cat in categoryCounts:
			categoryCounts[cat].append(float(b['stars']))
		else:
			categoryCounts[cat] = [float(b['stars'])]

averageRatings = {}
for cat in categoryCounts:
	avg = float(sum(categoryCounts[cat]))/float(len(categoryCounts[cat]))
	averageRatings[cat] = avg

everything = []
for rate in averageRatings:
	everything.append(averageRatings[rate])

print 'Total average of all business in Phoenix'
print sum(everything)/len(everything)

busFile.close()

jFile = open('../data/ratingAverages.json', 'wb')
json.dump(averageRatings, jFile)