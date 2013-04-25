import pandas as pd

df2010 = pd.read_csv('../data/cleanedData/2010LatLng.csv')

print df2010['Address'].describe()
print '__________________________________'
print df2010['Type'].describe()
print '__________________________________'
print df2010['Date'].describe()

#table = pivot_table(df2010, values='Date', )