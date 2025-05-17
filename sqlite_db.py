import sqlite3

# to work with SQLite we need to connect a database file with the program 
conn = sqlite3.connect(":memory:")
# now have to put cursor to work with it
cur = conn.cursor()

"Creating Table in SQLite"

# now using cur.execute("") we can give SQLite command 
cur.execute("CREATE TABLE students (Name TEXT, Age INTEGER, ID_NO TEXT)")
# now finish command with cur.commit()
conn.commit()

"Adding data in the table - 1st way"
# take input for data
name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
id_no1 = input("Enter your ID NO: ")

cur.execute("INSERT INTO students VALUES (:name, :age, :id_no)", {"name": name1, "age": age1, "id_no": id_no1}) # insert data
conn.commit() # commit changes

"Adding data in the table - 2nd way"

#take input for data
name2 = input("Enter your name: ")
age2 = int(input("Enter your age: "))
id_no2 = input("Enter your ID NO: ")

cur.execute("INSERT INTO students VALUES (?, ?, ?)", (name2, age2, id_no2)) # insert data
conn.commit() # commit changes

"Getting data from database - 1st way"

searched_name1 = input("Enter the name for what's you're looking for: ")

cur.execute(f"SELECT * FROM students WHERE name = :name", {"name": searched_name1}) # search for data with queries 
print(cur.fetchall()) # print data

"Getting data from database - 2nd way"

searched_name2 = input("Enter the name for what's you're looking for: ")

cur.execute(f"SELECT * FROM students WHERE name = ?", (searched_name2, )) # search for data with queries 
print(cur.fetchall()) # print data

"Order the Data from database"

cur.execute("SELECT rowid, * FROM students ORDER BY name") # ordering the data by name ascending order 
print(cur.fetchall())

cur.execute("SELECT rowid, * FROM students ORDER BY name DESC") # ordering the data by name descending order 
print(cur.fetchall())


# now have to close the file
conn.close()
