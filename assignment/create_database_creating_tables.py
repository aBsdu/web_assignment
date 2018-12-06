import mysql.connector

conn = mysql.connector.connect(user='root',password='Bsdu@123',host='localhost')

mycursor = conn.cursor()

mycursor.execute("""CREATE DATABASE mydatabase""")

mycursor.execute("""USE DATABASE mydatabase""")

mycursor.execute("""CREATE TABLE mytable(myid INTEGER,name TEXT, school TEXT)""")

mycursor.execute("""INSERT INTO mytable({},'{}','{}')""".format(my_id,name,school))
