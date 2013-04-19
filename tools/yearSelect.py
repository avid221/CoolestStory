'''
RUN:
python yearSelect.py > [whateverFileYouWant].json
'''

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

for crime in yearlyCrime:
	print crime
