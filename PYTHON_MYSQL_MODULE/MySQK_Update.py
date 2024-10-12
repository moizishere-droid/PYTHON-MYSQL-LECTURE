# UPDATE THE DATA IN THE TABLE OF THE PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "update users set name=\'aqsa\' where name=\'rafay\'"
my_cursor.execute(query)
mydb.commit()
my_cursor.close()
mydb.close()



# UPDATE THE DATA IN THE TABLE OF THE PARTICULAR DATABASE  --> PREVENT SQL INJECTION
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
user_input1 = input("Enter the name of the data that you want to change from: ")
user_input2 = input("Enter the name of the data that you want to change to : ")
query = "update users set name = %s where name like %s"
my_cursor.execute(query,(user_input2, "%" + user_input1 + "%"))
mydb.commit()
my_cursor.close()
mydb.close()