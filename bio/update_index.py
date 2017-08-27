import json
import os

html_temp = """
<!DOCTYPE html>
<html>
<head> 
	<title>bio Index</title>
    <!-- js libraries -->
	<link rel="stylesheet" href="../style.css">
</head>
<body id="bio_index">
<ul>

_text_
</ul>
</body>
</html>
"""

text_path = os.path.dirname(os.path.realpath(__file__)) + '/files'
file_list = os.listdir(text_path)
file_list.reverse()
html_txt = ""

for file in file_list:
	if os.path.splitext(file)[1] == ".html":
		html_txt += "<li><a href=files/" + file+ ">" + os.path.splitext(file)[0] + ".txt" + "</a></li>\n"
	else:
		html_txt += "<li><a href=files/" + file + ">" + file + "</a></li>\n"


html_str = html_temp.replace("_text_", html_txt)

Html_file = open(("bio_index.html"), "w")
Html_file.write(html_str)
Html_file.close()

