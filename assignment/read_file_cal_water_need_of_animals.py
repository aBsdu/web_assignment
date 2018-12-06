import csv
myDict={}

with open("zoo.csv") as csv_file:
    csv_read=csv.reader(csv_file,delimiter=",")
    next(csv_read)
    for row in csv_read:
        if row[0] not in myDict.keys():
            myDict[row[0]]=int(row[2])
        else:
            myDict[row[0]] = myDict[row[0]] + int(row[2])
#print "total water need of all the animals \n", myDict        
for key,values in myDict.items():
    print key,values
            
        
        
            
