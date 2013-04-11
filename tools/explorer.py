import pandas as pd
import ast
import json

crime = open('../data/cleanedCrimeData.json', 'rb')
crimeData = []
for line in crime:
	crimeData.append(ast.literal_eval(line))
crime.close()

crimeFrame = pd.DataFrame(crimeData)
print '====================CRIME======================='
print crimeFrame.describe()
del(crimeData)
del(crimeFrame)

yelpBusiness = open('../data/yelp_phoenix_academic_dataset/yelp_academic_dataset_business.json', 'rb')
businessData = []
for line in yelpBusiness:
	businessData.append(json.loads(line))
yelpBusiness.close()

businessFrame = pd.DataFrame(businessData)
print '====================BUSINESS===================='
print businessFrame.describe()
del(businessData)
del(businessFrame)

'''yelpCheckin = open('../data/yelp_phoenix_academic_dataset/yelp_academic_dataset_checkin.json', 'rb')
checkinData = []
for line in yelpCheckin:
	checkinData.append(json.loads(line))
yelpCheckin.close()

checkinFrame = pd.DataFrame(checkinData)
print '====================CHECKIN====================='
print checkinFrame.describe()
del(checkinData)
del(checkinFrame)'''

yelpReview = open('../data/yelp_phoenix_academic_dataset/yelp_academic_dataset_review.json', 'rb')
reviewData = []
for line in yelpReview:
	reviewData.append(json.loads(line))
yelpReview.close()

reviewFrame = pd.DataFrame(reviewData)
print '====================REVIEW======================'
print reviewFrame.describe()
del(reviewData)
del(reviewFrame)

yelpUser = open('../data/yelp_phoenix_academic_dataset/yelp_academic_dataset_user.json', 'rb')
userData = []
for line in yelpUser:
	userData.append(json.loads(line))
yelpUser.close()

userFrame = pd.DataFrame(userData)
print '====================USER========================'
print userFrame.describe()
del(userData)
del(userFrame)