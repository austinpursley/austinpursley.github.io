import os
import csv
from update_html import update_html
from datetime import datetime
from update_data import update_data

ask_if_new = input("add new tweet? enter y for yes ")
if ask_if_new == 'y':
    update_data()
##    with open('data.csv','a', newline='') as data:
##        date = input("squawk date: ")
##        datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
##        date = datetime.strftime(datetime_obj, '%Y%m%d%H%M')
##        print(date)
##        text = input("squawk: ")
##        sqwk_id = "squawk_" + date
##        print(date, text, sqwk_id)
##        new_squawk_row = [text, date, sqwk_id]
##        writer = csv.writer(data)
##        writer.writerow(new_squawk_row)
##
##    with open('data.csv', 'r', newline='') as data:
##        # reader = csv.reader(open('data.csv', 'r', newline=''))
##        reader = csv.reader(data)
##        next(reader, None)
##        sortdata = sorted(reader, key=lambda row: datetime.strptime(row[1], '%Y%m%d%H%M'))
##
##    with open('data.csv', 'w', newline='') as data:
##        writer = csv.writer(data, quoting=csv.QUOTE_ALL)
##        writer.writerows(sortdata)
else:
	print('not adding new tweet')

update_html()
