import csv
import pandas as pd
# from more_itertools import unique_everseen


# myCsvRow = [['1','Babin']]
# import os.path
# if os.path.isfile('csvexample.csv') == False:
# 	myFile = open('csvexample.csv','w')
# 	myData = [['ID','Name']]
# 	with myFile:
# 	    writer = csv.writer(myFile)
# 	    writer.writerows(myData)


# file = open('csvexample.csv','a')


# with file:
#     writers = csv.writer(file)
#     writers.writerows(myCsvRow)


# df = pd.read_csv('csvexample.csv')
# a = df.drop_duplicates(subset=['Name'],keep='first')
# a.to_csv('csvexample2.csv')
 
# df=pd.read_csv("StudentDetails.csv")
df=pd.read_csv("studentdups.csv")
# df = df.drop('Unnamed: 0', axis=1)
for items in df['ID']:
	if items == 1:
		print("ID is already chosen")
print(df['ID'])
# print(df.columns.values)



