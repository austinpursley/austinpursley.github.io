import csv
from datetime import datetime
def new_squawk():
    #get new squawk from user, write to data
    #(what newline='' means: https://docs.python.org/3/library/functions.html#open)
    with open('data.csv','a', newline='') as data:
        date = input("squawk date (e.g. '2016-03-15 13:53'): ")
        datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
        date = datetime.strftime(datetime_obj, '%Y%m%d%H%M')
        text = input("squawk: ")
        sqwk_id = "squawk_" + date
        print(date, text, sqwk_id)
        new_squawk_row = [text, date, sqwk_id]
        writer = csv.writer(data)
        writer.writerow(new_squawk_row)