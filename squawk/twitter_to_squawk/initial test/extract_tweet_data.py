import csv
from datetime import datetime
#trying to extract tweets and their date from "tweets archive" downloaded
#from twitter account
#def extract_data():
with open('data.csv', "r+", newline='') as data:
    with open('tweets 03 2019.csv', "r+", newline='') as tweets:
        reader = csv.reader(tweets)
        next(reader, None)  # skip the headers
        index_mid = ""
        i = 0
        for row in reversed(list(reader)):
            print(i)
            i+=1
            text = row[5]
            print(text)
            
            datetime_obj = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            date = datetime.strftime(datetime_obj, '%Y%m%d%H%M')
            squawk_id = "squawk_" + date
            new_row = [text, date, squawk_id]
            writer = csv.writer(data)
            writer.writerow(new_row)
##            id = row[2]
##            file_name = id + '.html'
##            
##            text = text.replace("\\n", "<br>")
##            date = row[1]
##            datetime_obj = datetime.strptime(date, '%Y%m%d%H%M')
##            index_date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
##
##            index_mid_part = html_index_mid_temp.replace("squawk_page", file_name)
##            index_mid_part = index_mid_part.replace("date", index_date_format)
##            index_mid_part = index_mid_part.replace("sqwk_text", text)
##            index_mid += index_mid_part
##
##        html_str = html_index_start + index_mid + html_index_end
##        Html_file = open("squawker.html", "w")
##        Html_file.write(html_str)
##        Html_file.close()
