import csv
from datetime import datetime

with open('data.csv','r', newline='') as data:
    reader = csv.reader(data)
    for row in reader:
        file_name = row[2] + ".html"
        if not os.path.exists(file_name):
            with open(file_name, 'w') as html_file:
