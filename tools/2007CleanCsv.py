import csv

files = range(1,13)

for f in files:
	path = '../data/2007/2007-%s.csv' % f
	f = open(path, 'rb')
	data = csv.DictReader(f)

	dictFile = open('../data/cleanedData/2007LatLng.json', 'ab')
	for d in data:
		if 'PHOENIX, AZ' in d['Address']:
			newLine = str(d)
			newLine += '\n'
			dictFile.write(newLine)