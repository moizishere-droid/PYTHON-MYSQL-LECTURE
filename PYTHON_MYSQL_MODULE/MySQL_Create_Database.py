#   CREATE DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="haseeb725"
)
my_cursor = mydb.cursor()
my_cursor.execute("Create Database moiz_practice") 
my_cursor.close()
mydb.close()



#   CHECK DATABASE IS CREATED OR NOT
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="haseeb725"
)
my_cursor = mydb.cursor()
my_cursor.execute("Show Databases") 
for a in my_cursor:
    print(a)
my_cursor.close()
mydb.close()



# AFTER CHECKING THE DATABASE EXIST , ADD THE DATABASE TO THE mydb , TO WORK ON IT
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
my_cursor.close()
mydb.close()



# YOU CAN ACCESS MULTIPLE DATABASE IN A SINGLE FILE 
import mysql.connector
mydb1 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="haseeb725",
    database = "moiz_practice"
)
mydb2 = mysql.connector.connect(
    host = "moiz_host",
    user = "Restro",
    password ="haseeb725",
    database = "mydatabase"
)
my_cursor1 = mydb1.cursor()
my_cursor2 = mydb2.cursor()
my_cursor1.close()
my_cursor2.close()
mydb1.close()
mydb2.close()