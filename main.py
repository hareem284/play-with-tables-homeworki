#JUST TO BE CLEAR I FOLLOWED THE INSTRUCTION BUT I PRITED LESS THINGS IF ITS NOT WORKING JUST HAVE THIS IN MIND I READ THE INSTRUCTIONS.


#importing sqlite3
import sqlite3
#importing pandas
import pandas as pd
connection=sqlite3.connect("basketball.sqlite")
print("lucky you connection is established and at the end get out here!!!!!!!!!!!!!!!")
chaeking=pd.read_sql("SELECT * FROM sqlite_master;",connection)
# moving on to reading the file and some other stuff
tables=pd.read_sql("SELECT * FROM Team;",connection)
print(tables)
tablescd=pd.read_sql("SELECT * FROM Full_name;",connection)
print(tablescd)
tableanoyed=pd.read_sql("SELECT * FROM Year_founded;",connection)
print(tableanoyed)
readcity=pd.read_sql("SELECT * FROM Team WHERE Full_name LIKE "LOS%";",connection)
print(readcity)
checkingmin=pd.read_sql("SELECT MIN(Year_founded)FROM Team",connection)
print(checkingmin)
chekingmax=pd.read_sql("SELECT MAX(Year_founded)FROM Team",connection)
print(chekingmax)