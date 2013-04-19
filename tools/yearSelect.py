import ast
import json

f = open('../data/cleanedCrimeData.json', 'rb')

yearlyCrime = []
YEAR = 11 #Place year here.

for line in f:
	crime = ast.literal_eval(line)
	month, day, year = crime['date'].split('/')
	if int(year) == YEAR:
		yearlyCrime.append(crime)

f.close()

newFile = open('../data/2011_DATA.json', 'wb')

json.dump(yearlyCrime, newFile)