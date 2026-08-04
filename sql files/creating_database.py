import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="WATER"
)

print("Connected successfully!")

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS WATER")
cursor.execute("USE WATER")
cursor.execute ("create table if not exists winfo(id int, FRIST_NAME varchar(50),LAST_NAME varchar(20),EMAIL varchar(30),DATE_OF_BIRTH date);")
try:
    cursor.execute("""
    INSERT INTO winfo VALUES
    (1,'kishor','holambe','offic.k@gmail.com','2008-01-01'),
    (2,'rahan','sayyed','offic.rehan@gmail.com','2007-12-01'),
    (3,'jagannth','phad','offic.j@gmail.com','2008-05-15'),
    (4,'rushi','hadabe','offic.rushi@gmail.com','2008-01-01'),
    (5,'rohit','kshirsager','offic.rohit@gmail.com','1998-01-22'),
    (6,'ganesh','phad','offic.ganesh@gmail.com','2006-11-22')
    """)
    conn.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print("Error:", err)
cursor.close()
conn.close()