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
# df=pd.read_csv("studentdups.csv")
# df = df.drop('Unnamed: 0', axis=1)

# a =4	

# for items in df['ID']:
# 	if items == int(a) :
# 		a =1 
# if a==1:
# 	print("ID is already chosen")		
# 	# print(df['ID'])
# # print(df.columns.values)


# id=3
# df=pd.read_csv("studentdups.csv")
# a = df[(df==id).any(1)]
# print(a)
# if a.empty:
# 	print("donot exist")
	
# else:
# 	print("Id exist")


# if int(a) in df['ID'].values:
# 	print("ID chosen")
# else:
# 	print("not chosen")

name = "suraj"
id = 1
a = name+'_'+str(id)
print(a)
df=pd.read_csv("studentdups.csv")
b = df[df['Name'] == a].index
df = df.drop(b)
df.to_csv('studentdups.csv')
print(df)
