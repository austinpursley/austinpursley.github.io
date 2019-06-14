import os
import json
from datetime import datetime

html_temp = """
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

with open('data.json', "r+") as data_file:
    data = json.load(data_file)
    for i in data['set']:
        # write html files for each squawk page according to json
        id = i['id']
        file_name = id + '.html'
        text = i['text']
        date = i['date']
        datetime_obj = datetime.strptime(date, '%Y%m%d%H%M%S')
        date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        html_str = html_temp.replace("sqwk_id", id)
        html_str = html_str.replace("sqwk_text",text)
        html_str = html_str.replace("sqwk_date", date)
        Html_file = open(file_name, "w")
        Html_file.write(html_str)
        Html_file.close()

    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()