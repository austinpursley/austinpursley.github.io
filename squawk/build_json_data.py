import os
import json

html_temp = """
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="../style.css">
	<!-- <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 850px) and (min-aspect-ratio: 1/1)" />
	
</head>
<body id="squawk_page">
	<p>squawk_content</p>
</body>
</html>
"""
# json and python
# import name from json, have all files written with that name
# edit the string to respective whatever

with open('data.json', "r+") as data_file:
    data = json.load(data_file)

    for i in data['set']:
        # Update directories according to JSON data.
        newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
        newpath += i['id']
        print(newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        # thought: prompt user, ask if they would like to add some photos here.
        # Update JSON data, img_array, according to imgages in directory.
        i['img_array'] = os.listdir(newpath)
        i['href'] = i['id'] + '.html'
        # write html files for each hike page according to json
        id = i['id']
        file_name = id + '.html'
        squawk_text = i['text']
        html_str = html_temp.replace("title2", title2)
        html_str = html_str.replace("img_array0", img_array0)
        html_str = html_str.replace("this_id", id)
        Html_file = open(file_name, "w")
        Html_file.write(html_str)
        Html_file.close()

    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()