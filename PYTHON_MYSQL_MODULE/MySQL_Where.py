# PRINT THE DATA OF THE TABLE IN A PARTICULAR DATABASE WITH SOME CONDITION APPLIED
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users where gender=\"male\""
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)


# PRINT THE DATA OF THE TABLE IN A PARTICULAR DATABASE WITH SOME WILDCARD CHARACTER --> give all the result than contain that phase or character
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users where name like \"%a%\" "
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)

# PREVENT SQL INJECTION FOR SAFE USER INPUT AND SECURITY
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="haseeb725",
    database="moiz_practice"
)
my_cursor = mydb.cursor()
user_input = input("Enter the name, character, or phrase you want to search in the name column: ")
query = "SELECT * FROM users WHERE name LIKE %s"
my_cursor.execute(query , ("%"+user_input+"%",))
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydb.close()