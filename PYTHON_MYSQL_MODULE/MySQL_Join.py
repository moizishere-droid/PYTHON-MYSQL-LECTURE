import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "moiz_practice"
)
cursor = mydb.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_id INT
)
""")

# Create departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
)
""")

# Insert sample data into employees table
cursor.execute("INSERT INTO employees (name, department_id) VALUES (%s, %s)", ("Alice", 1))
cursor.execute("INSERT INTO employees (name, department_id) VALUES (%s, %s)", ("Bob", 2))
cursor.execute("INSERT INTO employees (name, department_id) VALUES (%s, %s)", ("Charlie", None))

# Insert sample data into departments table
cursor.execute("INSERT INTO departments (department_name) VALUES (%s)", ("HR",))
cursor.execute("INSERT INTO departments (department_name) VALUES (%s)", ("Engineering",))


# Commit the transaction
mydb.commit()


# Perform INNER JOIN
inner_join_query = """
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id
"""

cursor.execute(inner_join_query)

# Fetch and print results
print("INNER JOIN Results:")
for row in cursor.fetchall():
    print(row)


# Perform LEFT JOIN
left_join_query = """
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
"""

cursor.execute(left_join_query)

# Fetch and print results
print("\nLEFT JOIN Results:")
for row in cursor.fetchall():
    print(row)



# Perform RIGHT JOIN
right_join_query = """
SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id
"""

cursor.execute(right_join_query)

# Fetch and print results
print("\nRIGHT JOIN Results:")
for row in cursor.fetchall():
    print(row)



# Simulate FULL OUTER JOIN using UNION
full_outer_join_query = """
(SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id)
UNION
(SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id)
"""

cursor.execute(full_outer_join_query)

# Fetch and print results
print("\nFULL OUTER JOIN Results:")
for row in cursor.fetchall():
    print(row)


# Close the cursor
cursor.close()
mydb.close()