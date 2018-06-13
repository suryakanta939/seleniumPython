import csv

def readData(fileName):

    # get one empty list
    data=[]
    # open the csv file
    dataFile=open(fileName,"r")
    # read the data from csv
    reader=csv.reader(dataFile)
#    skipp the header

    next(reader)
#     add rows from reader to empty list
    for row in reader:
        data.append(row)

    return data
