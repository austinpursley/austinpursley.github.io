import csv
from datetime import datetime

def update_data():
    # get new index number
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        #returns row with highest column 3 (index)
        maxnum = max(reader, key=lambda row: int(row[2])) 
        new_index = int(maxnum[2]) + 1
        print("new question index: " + str(new_index))
    
    # get data for new question from user and write to csv file
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
        new_question_row = [date, question, new_index]
        writer = csv.writer(data)
        writer.writerow(new_question_row)
    
    with open('data.csv', 'r', newline='') as data:
        # reader = csv.reader(open('data.csv', 'r', newline=''))
        reader = csv.reader(data)
        sortdata = sorted(reader, key=lambda row: datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
    
    # tells number of questions after new one
    # with open('data.csv', 'r', newline='') as data:
        # numline = sum(1 for row in data)
        # print('number of question after: ' + str(numline))
