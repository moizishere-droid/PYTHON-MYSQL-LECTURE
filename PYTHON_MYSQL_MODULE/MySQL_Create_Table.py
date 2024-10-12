# CREATE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "create table if not exists users (name varchar(255) , address varchar(255) , gender varchar (10) , married varchar(10))"
my_cursor.execute(query)
my_cursor.close()
mydb.close()


# CHECK TABLE IN A PARTICULAR DATABASE THAT ITS BEEN CREATED OR NOT
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "show tables"
my_cursor.execute(query)
for a in my_cursor:
    print(a)
my_cursor.close()
mydb.close()



# ADD THE PRIMARY KEY TO THE TABLE --> 1) AT THE TIME OF CREATION 2) AFTER CREATION
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "create table moiz ( ID int auto_increment primary key , name varchar(222) , address varchar(222), gender varchar(222))"
my_cursor.execute(query)
my_cursor.close()
mydb.close()

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "alter table users add column ID int auto_increment primary key"
my_cursor.execute(query)
my_cursor.close()
mydb.close()
