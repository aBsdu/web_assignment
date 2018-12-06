import sqlite3
import csv

conn = sqlite3.connect('std2.db') #conn is the pointer of database you created

c = conn.cursor()

#creating table for each csv file
#=======================================================================
'''
c.execute("""CREATE TABLE animal_table100( animal TEXT,
                                   uniq_id INTEGER,
                                   water_need INTEGER)""")

c.execute("""CREATE TABLE student_table99(StLastName TEXT ,
                                        StFirstName TEXT,
                                        Grade TEXT,
                                        Classroom INTEGER,
                                        Bus INTEGER)""")


c.execute("""CREATE TABLE student_table97(lastname TEXT,
                                            firstname TEXT,
                                            grade TEXT,
                                            classroom INTEGER)""")


c.execute("""CREATE TABLE air_table98(Id INTEGER,
                                    Airline TEXT ,
                                    Abbreviation TEXT,
                                    Country TEXT)""")
'''
#===========================================================================


# user choices
print ("press 1 for zoo database")
print ("press 2 for students database")
print ("press 3 for list database")
print ("press 4 for car makers database")


user_input= input("choose any of number to view that file data>>")
        

#===========================================================================
#               defining the function for zoo file
#===========================================================================
def zoo():
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            c.execute("""INSERT INTO animal_table100 VALUES('{}',{},{})""".format(row[0],row[1],row[2]))
    c.execute("SELECT * FROM animal_table100")
    return (c.fetchall())

#=======================================================================
#               defining the function for students file
#===========================================================================
def std():
    with open("List.csv") as csv_file2:
        csv_reader2 = csv.reader(csv_file2,delimiter=',')
        next(csv_reader2)
        for row2 in csv_reader2:
            c.execute("""INSERT INTO student_table99 VALUES('{}','{}','{}',{},{})""".format(row2[0],row2[1],row2[2],row2[3],row2[4]))
    c.execute("SELECT * FROM student_table99")
    return (c.fetchall())

#===========================================================================
#               defining the function for the list file
#===========================================================================
def air():
    with open("airlines.csv") as csv_file3:
        csv_reader3 = csv.reader(csv_file3,delimiter=',')
        next(csv_reader3)
        for row3 in csv_reader3:
            c.execute("""INSERT INTO air_table98 VALUES({},'{}','{}','{}')""".format(row3[0],row3[1],row3[2],row3[3]))
    c.execute("SELECT * FROM air_table98")
    return (c.fetchall())

#===========================================================================
#               defining the function for the carmaker file
#===========================================================================
def car():
    with open("students.csv") as csv_file4:
        csv_reader4 = csv.reader(csv_file4,delimiter=',')
        next(csv_reader4)
        for row4 in csv_reader4:
            c.execute("""INSERT INTO student_table97 VALUES('{}','{}','{}',{})""".format(row4[0],row4[1],row4[2],row4[3]))
    c.execute("SELECT * FROM student_table97")
    return (c.fetchall())

#===========================================================================
#===========================================================================

if user_input == 1:
    print zoo()
elif user_input == 2:
    print std()
elif user_input == 3:
    print air()
elif user_input == 4 :
    print car()

