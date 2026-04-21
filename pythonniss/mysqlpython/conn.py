import mysql.connector
con = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="niis"
)
if con:
	print("connected")
else:
	("not connected")