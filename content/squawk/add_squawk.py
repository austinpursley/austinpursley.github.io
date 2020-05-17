import os
from datetime import datetime
import glob



def new_squawk():
    #get new squawk from user, write to data
    #(what newline='' means: https://docs.python.org/3/library/functions.html#open)
    
    html_str = """
<!DOCTYPE html>
<html>

    <head> 
        <title> __squawk_id__ </title>
        <link rel="stylesheet" href="../style.css">
        <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 800px)">
        <time>__date__</time>
    </head>

    <body id="squawk_page">
        <p>__text__</p>
    </body>
</html>
	        
"""

    with open('data.csv','a', newline='') as data:
        print("input squawk date e.g. '2016-03-15 13:53'")
        print('or just "current", "c" for the current date & time')
        date = input("date: ")
        if date == "current" or date == "c":
            datetime_obj = datetime.now()
        else:
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
        date = datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M')
        text = input("squawk: ")
        sqwk_id = "squawk_" + datetime.strftime(datetime_obj, '%Y%m%d%H%M')
        print(date, text, sqwk_id)

        html_str = html_str.replace("__squawk_id__", sqwk_id)
        html_str = html_str.replace("__date__", date)
        html_str = html_str.replace("__text__", text)

        print(html_str)

        new_sqk_f_name = sqwk_id + ".html"
        pattern = '*.html'
        all_sqk_file_names = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
        if new_sqk_f_name in all_sqk_file_names:
            r_u_sure = input("file already exist for date. enter 'yes' to continue and overwrite that file: ")
            if r_u_sure == "yes":
                with open(new_sqk_f_name, "w+") as f:
                    f.write(html_str)
            else:
                print('file not overwritten. try again with a different date')
                raise SystemExit(0)
        else:
            with open(new_sqk_f_name, "w+") as f:
                f.write(html_str)
            


new_squawk()
