# SORT THE DATA --> DEFAULT IN ASCENDING ORDER
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users order by name"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)



# SORT THE DATA --> DESCENDING ORDER
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users order by name desc"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)