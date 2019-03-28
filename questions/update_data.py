import csv
from datetime import datetime

def update_data():
    # with open('data.csv') as data:
        # numline = sum(1 for row in data)
        # print('number of question before: ' + str(numline))
    with open('data.csv', 'a', newline='') as data:
        date_in = input("\nQuestion Date?:\noption1: %Y-%m-%d %H:%M\noption2: 'today' or 'now' for current timestamp\n\nDATE: ")
        if date_in ==  "today" or date_in == 'now':
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            datetime_obj = datetime.strptime(date_in, '%Y-%m-%d')
            date = datetime.strftime(datetime_obj, '%Y-%m%-&d %H:%M:%S')
        print(date)
        question = input("questions: ")
        print(date, question)
        new_question_row = [date, question]
        writer = csv.writer(data)
        writer.writerow(new_question_row)

    # with open('data.csv', 'r', newline='') as data:
        # numline = sum(1 for row in data)
        # print('number of question after: ' + str(numline))
    
    with open('data.csv', 'r', newline='') as data:
        # reader = csv.reader(open('data.csv', 'r', newline=''))
        reader = csv.reader(data)
        sortdata = sorted(reader, key=lambda row: datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))

    # with open('data.csv', 'w', newline='') as data:
        # writer = csv.writer(data, quoting=csv.QUOTE_ALL)
        # writer.writerows(sortdata)
