# PRINT THE DATA OF THE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)



# PRINT THE SPECIFIED COLUMN OF THE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select name , address from users"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)



# PRINT THE ONE ROW ONLY OF THE TABLE IN A PARTICULAR DATABASE --> CALLED MULTIPLE TIME TO GET MULTIPLE DATA
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users"
my_cursor.execute(query)
result1 = my_cursor.fetchone()
result2 = my_cursor.fetchone()
result3 = my_cursor.fetchone()
print(result1)
print(result2)
print(result3)