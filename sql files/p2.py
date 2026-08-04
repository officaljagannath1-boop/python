import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="worki"
)

print("Connected successfully!")

cursor = conn.cursor()