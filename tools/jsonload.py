import ast

f = open('crimeData.json', 'rb')

data = []
for line in f:
	data.append(ast.literal_eval(line))

for row in data:
	temp = row['date']
	temp.split('.')
	print temp