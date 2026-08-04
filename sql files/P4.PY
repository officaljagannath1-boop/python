cursor = conn.cursor()

cursor.execute("""
CREATE TABLE STUDENT (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    AGE INT,
    CITY VARCHAR(30)
)
""")

print("Table Created Successfully!")
