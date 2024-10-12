# DROP TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "drop table users"
my_cursor.execute(query)
my_cursor.close()
mydb.close()


# DROP IF EXIT TABLE IN A PARTICULAR DATABASE --> TO AVOID ERROR
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "drop table if exists users"
my_cursor.execute(query)
my_cursor.close()
mydb.close()
