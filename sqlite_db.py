import sqlite3

# to work with SQLite we need to connect a database file with the program 
conn = sqlite3.connect("test.db")
# now have to put cursor to work with it
cur = conn.cursor()

"Creating Table in SQLite"

# now using cur.execute("") we can give SQLite command 
cur.execute("CREATE TABLE students (Name TEXT, Age INTEGER, ID_NO TEXT)")
# now finish command with cur.commit()
cur.commit()

"Adding data in the table"
# take input for data
name = input("Enter your name: ")
age = int(input("Enter your age: "))
id_no = input("Enter your ID NO: ")

cur.execute("INSERT INTO students VALUES (:name, :age, :id_no)", {"name": name, "age": age, "id_no": id_no}) # insert data
conn.commit() # commit changes

"Getting data from database"
searched_name = input("Enter the name for what's you're looking for: ")

cur.execute(f"SELECT * FROM students WHERE name = '{searched_name}'") # search for data with queries 
print(cur.fetchall()) # print data

# now have to close the file
conn.close()