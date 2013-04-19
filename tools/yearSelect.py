import ast
import json

f = open('../data/cleanedCrimeData.json', 'rb')

yearlyCrime = []
YEAR = 12 #Place year here.

for line in f:
	crime = ast.literal_eval(line)
	month, day, year = crime['date'].split('/')
	if int(year) == YEAR:
		yearlyCrime.append(crime)

f.close()

newFile = open('../data/YEAR_DATA.json', 'wb')

json.dump(yearlyCrime, newFile, indent=4, separators=(',', ': '))