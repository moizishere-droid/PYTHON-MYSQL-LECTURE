# GET THE LINITED AMOUNT OF DATA ONLY
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users limit 2"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydb.close()



# GET THE LINITED AMOUNT OF DATA ONLY --> WITRH SOME SPECIFIES POSITION
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "select * from users limit 2 offset 2"
my_cursor.execute(query)
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydb.close()
