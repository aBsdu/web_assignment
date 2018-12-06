# importing csv liabrary
import csv

counter = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0

with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    next(csv_reader)
# calculating the water need of all the animals  
    for row in csv_reader:
        if row[0]=="elephant":
        #    print row[0],row[2]
            counter += int(row[2])

        elif row[0]=="tiger":
       #     print row[0],row[2]
            counter_2 += int(row[2])

        elif row[0]=="zebra":
       #     print row[0],row[2]
            counter_3+= int(row[2])

        elif row[0]=="kangaroo":
      #      print row[0],row[2]
            counter_4 += int(row[2])

        elif row[0]=="lion":
     #       print row[0],row[2]
            counter_5 += int(row[2])

    print "total water_need of elephant : ",counter
    print "total water_need of tiger : ",counter_2
    print "total water_need of zebra : ",counter_3
    print "total water_need of  kangaroo : ",counter_4
    print "total water_need of lion : ",counter_5
    
