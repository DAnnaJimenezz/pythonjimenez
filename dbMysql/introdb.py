import mysql.connector

db=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

print(type(db))
cursor = db.cursor()
cursor.execute("show databases")
print(cursor)
for dbs in cursor:
    print(dbs)