import csv

f = open('../data/2011LatLng.csv', 'rb')
reader = csv.DictReader(f)
jsonFile = open('../data/2011LatLng.json', 'ab')

for line in reader:
	newLine = str(line)
	newLine += '\n'
	print line
	jsonFile.write(newLine)