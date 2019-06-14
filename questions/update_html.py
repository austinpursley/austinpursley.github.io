import os
import csv
import lxml
from bs4 import BeautifulSoup
from datetime import datetime

def update_html():
    
    # 
    # update question index
    #
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

    pages = [] #list of question pages, to see which ones to remove
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        index_mid = ""
        for row in reversed(list(reader)):
            # read data
            date = row[0]
            text = row[1]
            index = row[2]          
            # prepare data
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
            # text = (row[1]).replace("\\n", "") #doing it this way before, for some reason
            # using data, prepare HTML text
            id = 'question_' + index
            file_name =  id + '.html'
            index_mid_part = html_index_mid_temp.replace("question_page", file_name)
            index_mid_part = index_mid_part.replace("date", date_format)
            index_mid_part = index_mid_part.replace("question_text", text)
            index_mid += index_mid_part
            pages.append(file_name)
        html_str = html_index_start + index_mid + html_index_end
        # Write HTML text to file
        Html_file = open("questions.html", "w")
        Html_file.write(html_str)
        Html_file.close()
        
    # remove any pages that need to be
    files = os.listdir(os.curdir)
    for f in files:
        if f[:9] == 'question_':
            if f not in pages:
                os.remove(f)
    #
    # update question pages
    #
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
            # read data
            date = row[0]
            text = row[1]
            index = row[2]
            # prepare data
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
            # text = (row[1]).replace("\\n", "") #doing it this way before, for some reason
            # using data, prepare HTML text
            id = 'question_' + index
            file_name =  id + '.html'
            # update HTML text if it exists, otherwise write new text
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
            else:
                html_str = html_page_temp.replace("q_id", id)
                html_str = html_str.replace("question_text", text)
                html_str = html_str.replace("question_date", date)
            # write HTML text to file
            Html_file = open(file_name, "w")
            Html_file.write(html_str)
            Html_file.close()
            
