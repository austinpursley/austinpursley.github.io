import csv
import os
import glob
from datetime import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
import piexif

from build_html import *

### LIKES  ###
# HTML templates
html_start1 = """
    <!DOCTYPE html>
    <html>

"""

html_start2 = """
    <head>
        <link rel="stylesheet" href="_STYLE_">
        <link rel="stylesheet" href="_MSTYLE_" media="screen and (max-device-width: _MDW_)" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
"""

#	    <link rel="stylesheet" href="_M2STYLE_" media="screen and (max-device-width: _MDW2_)" />

html_start3 = """

    <body id="id_text">
    <top></top>
        <table>
"""

# HEADER
# "default" page header
mobile_max_dw = "800px"
mobile2_max_dw = "850px"
href_style = "../style.css"
href_m_style = "../mobile.css"
href_m2_style = "../mobile2.css"
# works because order or replacement does not matter. use ordered dictionary if does
# https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
mdw_dic = {"_MDW_" : mobile_max_dw, "_MDW2_": mobile2_max_dw, "_STYLE_" : href_style, 
           "_MSTYLE_" : href_m_style, "_M2STYLE_" : href_m2_style}
html_head = html_start2
for i, j in mdw_dic.items():
    html_head = html_head.replace(i, j) 

html_end = """
        </table>

    </body>

    </html>
"""


# INDEX
html_top_likes = """
    <div class="top">
               <a href="index.html"><img class="logo home" src="likes_logo.png"/> </a>
       </div>
"""

html_likes_entry_temp = """
        <tr class="like">
	    <td class="like"><a href="link_text">title_text</a></td>
        </tr>
    """

html_start = html_start1 + html_head + html_start3

id_text = "likes"
html_start_likes = html_start.replace("the_title", "likes")
html_start_likes = html_start_likes.replace("id_text", id_text)
html_start_likes = html_start_likes.replace("<top></top>", html_top_likes)
with open('likes.csv', "r+", newline='') as data:
    likes_mid = ""
    reader = csv.reader(data)
    for row in list(reader):
	    title = row[0]		
	    link = row[1]
	    html_likes_entry = html_likes_entry_temp.replace("link_text",link)
	    html_likes_entry = html_likes_entry.replace("title_text",title)
	    likes_mid += html_likes_entry

likes_mid_arr = []
likes_mid_arr.append(likes_mid)

build_html_pages(html_start_likes, likes_mid_arr, html_end, "likes")

# LIKES PAGES THAT ARE HTML FILES
# likes page header
href_style = "../../style.css"
href_m_style = "../../mobile.css"
href_m2_style = "../../mobile2.css"
mdw_dic = {"_MDW_" : mobile_max_dw, "_MDW2_": mobile2_max_dw, "_STYLE_" : href_style, 
           "_MSTYLE_" : href_m_style, "_M2STYLE_" : href_m2_style}
html_head_likes = html_start2
for i, j in mdw_dic.items():
    html_head_likes = html_head_likes.replace(i, j)
print(html_head_likes)
# go through html files in likes folder, insert header
pattern = 'likes/*.html'
head_soup = BeautifulSoup(html_head_likes, 'html.parser')
like_head = head_soup.find('head')
for like_html_page_fn in glob.glob(pattern):
    with open(like_html_page_fn, "r") as f:
#        print("*******************")
#        print(like_html_page_fn)
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
#        print(soup.find('head'))
#        print("-_-_-_-_-_-")
        page_head = soup.find('head')
        if page_head:
            page_head.replace_with(like_head)
#            print(soup.find('head'))
#        print("*******************")
        soup.prettify()
    with open(like_html_page_fn, "w") as f:
        f.write(str(soup))
