import re
import datetime
import urllib2
import requests
from bs4 import BeautifulSoup

#-----------------FUNCTIONS-----------------------------------------
def convertToDate(dateString):
	atts = dateString.split('/')
	if len(atts) < 3:
		return 'bad'

	month, day, year = dateString.split('/')
	return datetime.date(int(year), int(month), int(day))

#----------------CODE-----------------------------------------------
url = urllib2.urlopen('http://www.spotcrime.com/az/phoenix/daily/more')
content = url.read()
soup = BeautifulSoup(content)

allLinks = soup.find_all(href=re.compile("/az/phoenix/daily"))
cleanLinks = {}
for link in allLinks:
	dateForm = convertToDate(link.text)
	if dateForm == 'bad':
		continue
	elif dateForm.year < 2008:
		continue

	cleanLinks[dateForm] = link.get('href')

for link in cleanLinks:
	base = 'http://www.spotcrime.com'
	base += cleanLinks[link]

	#print base

	count = 0
	while count < 10:
		try:
			redPill = urllib2.urlopen(base)
			break
		except urllib2.URLError:
			count += 1
			continue

	content = redPill.read()
	soup = BeautifulSoup(content)

	table = soup.find_all('table')
	del(table[0])
	for row in table[0].find_all('tr'):
		cols = row.find_all('td')
		if len(cols) != 5:
			continue
		trash, crime, date, address, alsoTrash = cols
		instance = {'crime':crime.text, 'date':date.text, 'address':address.text}
		print instance