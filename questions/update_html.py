import os
import csv
import lxml
from bs4 import BeautifulSoup
from datetime import datetime

def update_html():
    
    # update question index
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
			    <time>date</time>  
            </td>
			<td>
				<a href="question_page">question_text</a>
			</td>
        </tr>
    """


    html_index_end = """
        </table>

        </body>

        </html>
    """

    pages = []
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        index_mid = ""
        for row in reversed(list(reader)):
            text = row[1]
            text = text.replace("\\n", "")
            date = row[0]
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
            date_html = datetime.strftime(datetime_obj, '%Y%m%d-%H%M%S')
            id = 'question_' + date_html
            file_name =  id + '.html'
            index_mid_part = html_index_mid_temp.replace("question_page", file_name)
            index_mid_part = index_mid_part.replace("date", date_format)
            index_mid_part = index_mid_part.replace("question_text", text)
            index_mid += index_mid_part
            pages.append(file_name)
        
        html_str = html_index_start + index_mid + html_index_end
        Html_file = open("questions.html", "w")
        Html_file.write(html_str)
        Html_file.close()

    # update question pages
    html_page_temp = """
            <!DOCTYPE html>
            <html>
            <head>
                <title> q_id </title>
                <link rel="stylesheet" href="../style.css">
                <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 800px)" />
            </head>
            <body id="question_page">
                <h1><div id="question">
                    question_text
                </div></h1>
                <time>question_date</time>
                <div id="answer">
                </div>
            </body>
            </html>
        """
        
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            # write html files for each question page according to json
            text = row[1]
            text = text.replace("\\n", "")
            date = row[0]
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
            date_html = datetime.strftime(datetime_obj, '%Y%m%d-%H%M%S')
            id = 'question_' + date_html
            file_name =  id + '.html'
            if os.path.isfile(file_name):
                print(file_name)
                with open(file_name) as fp:
                    soup = BeautifulSoup(fp, 'lxml')
                    soup.time.string = date_format
                    soup.title.string = id
                    question = soup.find("div", {"id": "question"})
                    question.string = text
                    html_str = soup.prettify()
                    print(soup.prettify()) 
                    # soup.time.replace_with(date)
                    # soup.find("div", {"id": "question"}).replace_with(question)
                    
                    # html_str = BeautifulSoup(fp, 'lxml')
                    # html_str = soup.replace("q_id", id)
                    # html_str = html_str.replace("question_text", text)
                    # html_str = html_str.replace("question_date", date)
                
                # new_title = id
                # new_date = date
                # new_question = 
                # print(title, date, question)
                # continue
            else:
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
            
