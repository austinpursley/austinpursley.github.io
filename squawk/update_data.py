import csv
from datetime import datetime
def update_data():
    # get number of rows in data, was useful for debugging
    # with open('data.csv') as data:
        # numline = sum(1 for row in data)
        # print('number of squawk before: ' + str(numline))
        
    #sort the data by date
    with open('data.csv', newline='') as data:
        # reader = csv.reader(open('data.csv', 'r', newline=''))
        reader = csv.reader(data)
        sortdata = sorted(reader, key=lambda row:datetime.strptime(row[1], '%Y%m%d%H%M'))
    #write new, sorted data to file
    with open('data.csv', 'w', newline='') as data:
        #QUOTE_ALL means all the data fields have quotes 
        writer = csv.writer(data, quoting=csv.QUOTE_ALL)
        writer.writerows(sortdata)
