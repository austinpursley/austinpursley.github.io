import os
import csv
from datetime import datetime

def update_html():
    html_index_start = """
    <!DOCTYPE html>
    <html>

    <head>
        <title> squawks </title>
        <link rel="stylesheet" href="../style.css">
        <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 850px)" />
        <link rel="stylesheet" href="../mobile_portrait.css" media="screen and (max-device-width: 500px)" />
    </head>

    <body id="squawk_index">

        <div class="top">
               <a href="../index.html"><img src="../squawk_logo.png"></img></a>
        </div>

        <table>
    """

    html_index_mid_temp = """
        <tr>
			<td>
			    <time><a href="squawk_page">date</a></time>
                <p>sqwk_text</p>
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
        <title> sqwk_id </title>
        <link rel="stylesheet" href="../style.css">
        <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 800px)" />
        <time>sqwk_date</time>
    </head>
    <body id="squawk_page">
        <p>sqwk_text</p>
    </body>
    </html>
    """
    #update squawk index
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        index_mid = ""
        for row in reversed(list(reader)):

            id = row[2]
            file_name = id + '.html'
            text = row[0]
            text = text.replace("\\n", "<br>")
            date = row[1]
            datetime_obj = datetime.strptime(date, '%Y%m%d%H%M')
            index_date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')

            index_mid_part = html_index_mid_temp.replace("squawk_page", file_name)
            index_mid_part = index_mid_part.replace("date", index_date_format)
            index_mid_part = index_mid_part.replace("sqwk_text", text)
            index_mid += index_mid_part

        html_str = html_index_start + index_mid + html_index_end
        Html_file = open("squawker.html", "w")
        Html_file.write(html_str)
        Html_file.close()

    #update squawk pages
    with open('data.csv', "r+", newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            # write html files for each squawk page according to json
            id = row[2]
            file_name = id + '.html'
            text = row[0]
            text = text.replace("\\n", "<br>")
            date = row[1]
            datetime_obj = datetime.strptime(date, '%Y%m%d%H%M')
            date = datetime_obj.strftime('%Y-%m-%d %H:%M')
            html_str = html_page_temp.replace("sqwk_id", id)
            html_str = html_str.replace("sqwk_text",text)
            html_str = html_str.replace("sqwk_date", date)
            Html_file = open(file_name, "w")
            Html_file.write(html_str)
            Html_file.close()