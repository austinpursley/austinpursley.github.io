import csv
import os
import glob
from datetime import datetime
import re
from bs4 import BeautifulSoup

def build_html_pages(html_start_str, mid_pages_arr, html_end_str, title):
	next_page_entry1 = """
		<tr class="nav">
			<td style="visibility: hidden;" class="nav_button"></td>
			<td class="nav_button"><a href="next_page_link">next page</a></td>
		</tr>
	"""
	next_page_entry2 = """
		<tr class="nav">
			<td class="nav_button"><a href="prev_page_link">prev page</a></td>
			<td class="nav_button"><a href="next_page_link">next page</a></td>
		</tr>
    	"""
	next_page_entry3 = """
		<tr class="nav">
			<td class="nav_button"><a href="prev_page_link">prev page</a></td>
			<td style="visibility: hidden;" class="nav_button"></td>
		</tr>
   	 """
	i = 1
	mid_num = len(mid_pages_arr)
	print(mid_num)
	if mid_num == 1:
		html_str = html_start_str + mid_pages_arr[0] + html_end_str
		Html_file = open(title + ".html", "w")
		Html_file.write(html_str)
		Html_file.close()	
	else:
		for mid in mid_pages_arr:
		
			if i == 1:
				Html_file = open(title + ".html", "w")
				mid += next_page_entry1.replace("next_page_link", title + "2.html")
			else:
				curr_page_link = title + str(i) + ".html"				
				next_page_link = title + str(i+1) + ".html"
				if i == 2:
					prev_page_link = title + ".html"
				else:
					prev_page_link = title + str(i-1) + ".html"
				if i == mid_num:
					mid_temp = next_page_entry3.replace("next_page_link", next_page_link)
				else:
					mid_temp = next_page_entry2.replace("next_page_link", next_page_link)
				mid += mid_temp.replace("prev_page_link", prev_page_link)
				Html_file = open(curr_page_link, "w")
					
			html_str = html_start_str + mid + html_end_str
			Html_file.write(html_str)
			Html_file.close()
			i += 1

with open('data.csv', "r+", newline='') as data:
	# Clear data.csv
	data.truncate(0)	
	#write data columns
	writer = csv.writer(data, quoting=csv.QUOTE_ALL)
	writer.writerow(['Date','Type','File-name','Text'])
	##### Images #####
	#set path of images directory
	#newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
	#newpath += 'images/'
	#get list of image file names from directory
	pattern = 'images/*.jpg'
	img_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
	for img in img_arr:
		img_no_ext = os.path.splitext(img)[0]
		# date should be encoded within file name
		dt = datetime.strptime(img_no_ext, '%Y%m%d%H%M')
		dt_str = datetime.strftime(dt, '%Y.%m.%d %I:%M %p')
		writer.writerow([dt_str, "image", img])
	##### squawks #####
	#get list of html file names from directory
	pattern = 'squawk/*.html'
	sqk_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
	for sqk in sqk_arr:
		sqk_no_ext = os.path.splitext(sqk)[0]
		dt = datetime.strptime(sqk_no_ext[-12:], '%Y%m%d%H%M')
		dt_str = datetime.strftime(dt, '%Y.%m.%d %I:%M %p')
		
		sqk_fdir = "squawk/" + sqk
		with open(sqk_fdir, "r") as f:
			contents = f.read()
			soup = BeautifulSoup(contents, 'html.parser')
			sqk_txt = "".join([str(item) for item in soup.p.contents])
			writer.writerow([dt_str, "squawk", sqk, sqk_txt])

#sort the data by date
with open('data.csv', newline='') as data:
	# reader = csv.reader(open('data.csv', 'r', newline=''))
	reader = csv.reader(data)
	next(reader, None) #skip header row
	sortdata = sorted(reader, key=lambda row:datetime.strptime(row[0], '%Y.%m.%d %I:%M %p'))
#write new, sorted data to file
with open('data.csv', 'w', newline='') as data:
	#QUOTE_ALL means all the data fields have quotes 
	writer = csv.writer(data, quoting=csv.QUOTE_ALL)
	writer.writerows(sortdata)


html_start = """
    <!DOCTYPE html>
    <html>

    <head>
        <title> the_title </title>
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="mobile.css" media="screen and (max-device-width: 850px)" />
        <link rel="stylesheet" href="mobile_portrait.css" media="screen and (max-device-width: 500px)" />
    </head>

    <body id="id_text">
    <top></top>
        <table>
    """

html_top_scroll = """
	<div class="top">
		<a href="../index.html"><img class="logo home" src="home_logo.png"/> </a>
	</div>
"""
html_top_image = """
	<div class="top">
               <a href="../index.html"><img class="logo home" src="images_logo.png"/></a>
       </div>
"""

html_top_squawk = """
	<div class="top">
               <a href="../index.html"><img class="logo home" src="squawk_logo.png"/> </a>
       </div>
"""

#html_top_image = """
#	<div class="top">
#           <div class="logo icon1">
#               <a href="squawks.html"><img src="squawk_logo.png"/> </a>
#           </div>
#	   <div class="logo icon2">
#               <a href="scroll.html"><img src="images_logo_grayed.png"/> </a>
#           </div>
#       </div>
#"""

#html_top_squawk = """
#	<div class="top">
#           <div class="logo icon1">
#               <a href="scroll.html"><img src="squawk_logo_grayed.png"/> </a>
#           </div>
#	   <div class="logo icon2">
#               <a href="images.html"><img src="images_logo.png"/> </a>
#           </div>
#       </div>
#"""
id_text = "content"
html_start_scroll = html_start.replace("the_title", "scroll")
html_start_scroll = html_start_scroll.replace("id_text", id_text)
html_start_scroll = html_start_scroll.replace("<top></top>", html_top_scroll)

id_text = "squawks"
html_start_squawk = html_start.replace("the_title", "squawks")
html_start_squawk = html_start_squawk.replace("id_text", id_text)
html_start_squawk = html_start_squawk.replace("<top></top>", html_top_squawk)

id_text = "images"
html_start_image = html_start.replace("the_title", "images")
html_start_image = html_start_image.replace("id_text", id_text)
html_start_image = html_start_image.replace("<top></top>", html_top_image)


html_image_entry_temp = """
	<tr class="content">
		<td class="date"><time>date_text</time></td>
		<td class="image"><a href="img_src"><img src="thumbnail_src"></a></td>
	</tr>
"""
html_squawk_entry_temp = """
        <tr class="content">
		<td class="date"><time>date_text</a></time></td>
		<td class="squawk"><a href="squawk_page">sqwk_text</a></td>
        </tr>
    """

html_end = """
        </table>

    </body>

    </html>
    """

pattern = '*.html'
f_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
for f in f_arr:
	print(f)
	os.remove(f)

#update scroll
with open('data.csv', "r+", newline='') as data:
	reader = csv.reader(data)
	scroll_mid = ""
	squawk_mid = ""
	image_mid = ""
	loops_thresh = 120 
	scroll_loop_count = 0
	squawk_loop_count = 0
	image_loop_count = 0
	mid_pages_arr = []
	mid_pages_sqwk_arr = []
	mid_pages_imgs_arr = []

	for row in reversed(list(reader)):
		date = row[0]		
		elem_type = row[1]		
		file_name = row[2]
		
#		text = text.replace("\\n", "<br>")
#		datetime_obj = datetime.strptime(date, '%Y.%m.%d %I:%M %p')
#		scroll_date_format = datetime.strftime(datetime_obj, '%Y.%m.%d %I:%M %p')
		if elem_type == "image":
			img_dir = "images/" + file_name
			thumbnail_dir = "images/thumbnail/" + file_name
			image_entry = html_image_entry_temp.replace("img_src", img_dir)
			image_entry = image_entry.replace("thumbnail_src", thumbnail_dir)
			image_entry = image_entry.replace("date_text", date)
			scroll_mid += image_entry
			image_mid += image_entry
			scroll_loop_count += 10
			image_loop_count += 10
		elif elem_type == "squawk":
			text = row[3]
			file_dir = "squawk/" + file_name
			squawk_entry = html_squawk_entry_temp.replace("squawk_page", file_dir)
			squawk_entry = squawk_entry.replace("date_text", date)
			squawk_entry = squawk_entry.replace("sqwk_text", text)
			scroll_mid += squawk_entry
			squawk_mid += squawk_entry
			scroll_loop_count += 1
			squawk_loop_count += 1
		
		if scroll_loop_count >= loops_thresh:
			scroll_loop_count = 0
			mid_pages_arr.append(scroll_mid)
			scroll_mid = ""
		if image_loop_count >= loops_thresh:
			image_loop_count = 0
			mid_pages_imgs_arr.append(image_mid)	
			image_mid = ""	
		if squawk_loop_count >= loops_thresh:
			squawk_loop_count = 0
			mid_pages_sqwk_arr.append(squawk_mid)
			squawk_mid = ""
	mid_pages_arr.append(scroll_mid)
	mid_pages_sqwk_arr.append(squawk_mid)
	mid_pages_imgs_arr.append(image_mid)
	build_html_pages(html_start_scroll, mid_pages_arr, html_end, "scroll")
	build_html_pages(html_start_image, mid_pages_imgs_arr, html_end, "images")
	build_html_pages(html_start_squawk, mid_pages_sqwk_arr, html_end, "squawks")
