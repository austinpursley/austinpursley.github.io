import os
import csv
from datetime import datetime

def update_html():
    html_index_start = """
		<!DOCTYPE html>
		<html>

		<head> 
			<title> questions </title>
			<link rel="stylesheet" href="style.css">
			<link rel="stylesheet" href="mobile.css" media="screen and (max-device-width: 850px)" />
			<link rel="stylesheet" href="mobile_portrait.css" media="screen and (max-device-width: 500px)" />
		</head>

		<body id="project_index">
			
		<h1>questions</h1>
			
		<table>
	"""

    html_index_mid_temp = """
        <tr>
            <td>
			    <time><a href="question_page">date</a></time>  
            </td>
			<td>
				question_text
			</td>
        </tr>
    """


    html_index_end = """
        </table>

        </body>

        </html>
    """

    html_page_temp = """
        <!DOCTYPE html>
        <html>
        <head>
            <title> q_id </title>
            <link rel="stylesheet" href="../style.css">
            <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 800px)" />
            <time>question_date</time>
        </head>
        <body id="question_page">
            <div id="question">
                <p>question_text</p>
            </div>
            <div id="answer">
            </div>
        </body>
        </html>
    """
    # update question index
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        index_mid = ""
        for row in reversed(list(reader)):
            text = row[1]
            text = text.replace("\\n", "")
            date = row[0]
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            index_date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
            date_html = datetime.strftime(datetime_obj, '%Y%m%d-%H%M%S')
            id = 'question_' + date_html
            file_name =  id + '.html'
            index_mid_part = html_index_mid_temp.replace("question_page", file_name)
            index_mid_part = index_mid_part.replace("date", index_date_format)
            index_mid_part = index_mid_part.replace("question_text", text)
            index_mid += index_mid_part
        
        html_str = html_index_start + index_mid + html_index_end
        Html_file = open("questions.html", "w")
        Html_file.write(html_str)
        Html_file.close()

    # update question pages
    pages = []
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            # write html files for each question page according to json
            text = row[1]
            text = text.replace("\\n", "")
            date = row[0]
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date_html = datetime.strftime(datetime_obj, '%Y%m%d-%H%M%S')
            id = 'question_' + date_html
            file_name =  id + '.html'
            pages.append(file_name)
            html_str = html_page_temp.replace("q_id", id)
            html_str = html_str.replace("question_text", text)
            html_str = html_str.replace("question_date", date)
            Html_file = open(file_name, "w")
            Html_file.write(html_str)
            Html_file.close()
    
    files = os.listdir(os.curdir)
    for f in files:
        if f[:9] == 'question_':
            if f not in pages:
                os.remove(f)
            
