import json
import os

html_temp = """
<!DOCTYPE html>
<html>
<head> 
	<title>_date_</title>
    <!-- js libraries -->
	<link rel="stylesheet" href="../../style.css">
</head>
<body id="bio">

_text_
</body>
</html>
"""

text_path = os.path.dirname(os.path.realpath(__file__)) + '/text_files'
txt_file_list = os.listdir(text_path)

for txt_file in txt_file_list:
    #open and read file
    f = open(("text_files/"+ txt_file), "r")
    #get array of lines from file
    lines = f.readlines()
    new_lines = []
    for i, line in enumerate(lines):
        if (line == "\n...") | (line == "...\n") | (line == "..."):
            new_lines.append("<p>...</p>\n")
        elif (line == '\n'):
            new_lines.append("<p></p>\n")
        else:
            new_lines.append("<p>" + line + "</p>\n")

    html_txt = ''.join(new_lines)
    date = os.path.splitext(txt_file)[0]
    html_str = html_temp.replace("_text_", html_txt)
    html_str = html_str.replace("_date_", date)
    Html_file = open(("files/" + date+".html"), "w")
    Html_file.write(html_str)
    Html_file.close()

#if txt file was removed from text_files folder, remove the respective html file
files_path = os.path.dirname(os.path.realpath(__file__)) + '/files'
files_list = os.listdir(files_path)
files_list_comp = []
for i, file_name in enumerate(files_list):
    if file_name[-5:] == ".html":
        files_list_comp.append(os.path.splitext(files_list[i])[0])
print(files_list_comp)

for i, file_name in enumerate(txt_file_list):
    txt_file_list[i] = os.path.splitext(txt_file_list[i])[0]
print(txt_file_list)

for file_name in files_list_comp:
        if not (file_name in txt_file_list):
            print(file_name)
            os.remove(files_path + "/" + file_name + ".html")
            #.remove(files_path + file_name)