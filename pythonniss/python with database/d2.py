import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("INSERT INTO student VALUES(2,'gita',95)")
conn.commit()
conn.close()
print("Data inserted successfully")