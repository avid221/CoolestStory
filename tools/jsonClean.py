import ast 

f = open('../data/crimeData.json')

data = []
for line in f:
	#json.dumps(line)
	data.append(ast.literal_eval(line))

for crime in data:
	crime['date'] = crime['date'].strip()
	dSplit = crime['date'].split('.')

	if dSplit[1] != '':
		date, time, trash = dSplit
		crime['date'] = date
		time = time.strip()
		crime['time'] = time
	else:
		date, trash = dSplit
		crime['date'] = date
		crime['time'] = 'none'

for crime in data:
	print crime
