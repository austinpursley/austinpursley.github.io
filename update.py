import json
import os
from datetime import datetime

html_str = """
<!DOCTYPE html>
<html>

<head> 
	<title> squawk </title>
	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" href="mobile.css" media="screen and (max-device-width: 850px)" />
	<link rel="stylesheet" href="mobile_portrait.css" media="screen and (max-device-width: 500px)" />
</head>

<body id="squawk_index">
	
	<h1>squawk</h1>
	
	<table>
	
"""


html_temp = """
	<tr>
		<td>
			<a href="squawk/squawk_DATE.html">TITLE</a>
		</td>
	</tr>
"""

html_str_end = """
		
	</table>
	
</body>

</html>
"""
#json and python
#import name from json, have all files written with that name
#edit the string to respective whatever

files_list = os.listdir('squawk')
files_list.reverse()

for file in files_list:

    date = file[7:-5]
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    hrmn = date[8:12]

    d = datetime.strptime(hrmn, "%H%M")
    hrmn = d.strftime("%I:%M %p")
    title = month + "." + day + "." + year + " " + hrmn
    print(title)

    html_rplc = html_temp.replace("DATE", date)
    html_rplc = html_rplc.replace("TITLE", title)

    html_str += html_rplc
    # print(html_rplc_mid)

html_str += html_str_end

Html_file = open('squawk.html', "w")
Html_file.write(html_str)
Html_file.close()

print(html_str)
