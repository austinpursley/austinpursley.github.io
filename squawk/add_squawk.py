import json
import csv
from datetime import datetime

with open('data.csv','a', newline='') as data:
    date = input("squawk date: ")
    text = input("squawk: ")
    sqwk_id = "squawk_" + date
    print(date, text, sqwk_id)
    new_squawk_row = [text, date, sqwk_id]
    writer = csv.writer(data)
    writer.writerow(new_squawk_row)
data.close()

data = csv.reader(open('data.csv', 'r', newline=''))
next(data, None)
sortdata = sorted(data, key=lambda row: datetime.strptime(row[1], '%Y%m%d%H%M%S'))

with open('data_sorted.csv', 'w', newline='') as newfile:
    writer = csv.writer(newfile)
    writer.writerows(sortdata)