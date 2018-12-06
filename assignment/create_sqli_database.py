# inporting sql liabrary
# sqllite is the database that is used for mobiles which create a single file database 
import sqlite3
import csv

#creating database (file based databased)

conn = sqlite3.connect('zoo.db') #conn is the pointer of database you created

# creating cursor
# cursor is used to send your sql query to the database.
# so we need to create a cursor in python
# all the remains work will be done by this CURSOR

c = conn.cursor()# 'c' is a cursor

# now creating the table using python and sql query
# here the c.execute is used to execute the sql query
# create table only one time
'''c.execute("""CREATE TABLE zoo_table101( animal TEXT,
                                   uniq_id INTEGER,
                                   water_need INTEGER)""")

'''

# importing zoo.csv data into table100
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        c.execute("""INSERT INTO zoo_table100 VALUES('{}',{},{})""".format(row[0],row[1],row[2]))
        
# to view the data of the table
c.execute("SELECT * FROM zoo_table100")
print (c.fetchall())

