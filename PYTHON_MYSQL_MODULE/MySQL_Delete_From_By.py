# DELETE THE DATA FROM THE TABLE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "delete from users where name='alisa'"
my_cursor.execute(query)
mydb.commit()
my_cursor.close()
my_cursor.close()


# DELETE THE DATA FROM THE TABLE WITH THE HELPOF PREVENT SQL INJECTION
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
user_input = input("Enter the name of the user that you want to delete: ")
query = "delete from users where name like %s"
my_cursor.execute(query,("%"+user_input+"%",))
mydb.commit()
my_cursor.close()
my_cursor.close()

