import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="niis"
)
print("Connected successfully")
cur = con.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
print("\nStudent Records:\n")
for r in rows:
    print("Roll No:", r[0])
    print("Name:", r[1])
    print("Marks:", r[2])
    print("------------------------")
con.close()