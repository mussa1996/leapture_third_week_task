import psycopg2

# # Connect to your postgres DB
# conn = psycopg2.connect("dbname=test user=postgres")

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query
# cur.execute("SELECT * FROM my_data")

# # Retrieve query results
# records = cur.fetchall()

import psycopg2

# url = "postgres://postgres:1234@localhost:5432/db_name"
# connection = psycopg2.connect(url)
# cursor = connection.cursor()

# cursor.execute("SELECT version();")
# version = cursor.fetchone()
# print(version)

# connection.close()

import psycopg2

con = psycopg2.connect(database='leapture', user='postgres',
                       password='mussa')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Skoda', 9000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Bentley', 350000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")