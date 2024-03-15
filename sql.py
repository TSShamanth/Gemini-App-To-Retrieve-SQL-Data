import sqlite3

# Connect to SQLite
connection = sqlite3.connect("students.db")

# Create a cursor object to insert records and create tables
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENTS (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENTS VALUES ('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Vikash', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Dipesh', 'DEVOPS', 'A', 35)''')

# Display all the records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENTS''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
