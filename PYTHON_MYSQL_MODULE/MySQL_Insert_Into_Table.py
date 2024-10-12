# INSERT A SINGLE DATA INTO THE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "insert into users (name,address,gender) values(%s,%s,%s)"
my_values = ("moiz","PIB","MALE")
my_cursor.execute(query,my_values)
mydb.commit()
print(my_cursor.rowcount , "no of row has been inserted")



# INSERT A MULTIPLE DATA INTO THE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "insert into users (name,address,gender) values(%s,%s,%s)"
my_values = [("RAFAY","DHA","MALE"),("ANAS","CHIFFON","MALE"),("AQSA","KU","FEMALE")]
my_cursor.executemany(query,my_values)
mydb.commit()
print(my_cursor.rowcount , "no of row has been inserted")



# GET THE ID OF THE DATA IN THE TABLE IN A PARTICULAR DATABASE
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
my_cursor = mydb.cursor()
query = "insert into users (name,address,gender) values(%s,%s,%s)"
my_values = [("ALISA","KQ","FEMALE")]
my_cursor.executemany(query,my_values)
mydb.commit()
print(my_cursor.rowcount , "no of row has been inserted")
print(my_cursor.lastrowid , "no of row has been inserted") # you will get only the id of the last data --> if you add many data