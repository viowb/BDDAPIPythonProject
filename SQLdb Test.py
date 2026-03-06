import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_ta25!wbY66@",
    database="mydb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

conn.close()