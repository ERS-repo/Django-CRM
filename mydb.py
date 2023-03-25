#https://dev.mysql.com/downloads/installer/
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'evan',
	passwd = 'R@d@c#P)'
	)

# prepare cursor object

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE crmBackend")

print("Complete")