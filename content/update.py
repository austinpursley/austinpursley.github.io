import csv
import os
import glob
from datetime import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
import piexif
import piexif.helper

def imgs_in_dir(in_dir, extensions = ("*.png","*.jpg","*.jpeg","*.JPG","*.gif",)):  
    img_arr = []
    for e in extensions:
        pattern = in_dir + e
        img_arr.extend(sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True))
    return sorted(img_arr, reverse=True)

def build_html_pages(html_start_str, mid_pages_arr, html_end_str, title):
    """ creates HTML pages given template pieces

    :param html_start_str: start of HTML page
    :param mid_pages_arr: list where each element is middle section for a new HTML file
    :param html_end_str: end of HTML page
    "param title: what the HTML file will be named
    """
    next_page_entry1 = """
    <table class="nav">
	    <tr>
		    <td style="visibility: hidden;" class="nav_button prev"></td>
		    <td class="nav_button next"><a href="next_page_link">next page</a></td>
	    </tr>
    </table>
    """
    next_page_entry2 = """
    <table class="nav">
	    <tr>
		    <td class="nav_button prev"><a href="prev_page_link">prev page</a></td>
		    <td class="nav_button next"><a href="next_page_link">next page</a></td>
	    </tr>
    </table>
	    """
    next_page_entry3 = """
    <table class="nav">
	    <tr>
		    <td class="nav_button prev"><a href="prev_page_link">prev page</a></td>
		    <td style="visibility: hidden;" class="nav_button next"></td>
	    </tr>
    </table>
    """
    mid_num = len(mid_pages_arr)
    print(mid_num)
    if mid_num == 1:
        #case where only writing one HTML page
        html_str = html_start_str + mid_pages_arr[0] + html_end_str
        Html_file = open(title + "1.html", "w")
        Html_file.write(html_str)
        Html_file.close()	
    else:
        #writing two or more HTML pages
        for page_num, mid in enumerate(mid_pages_arr, 1):
            if page_num == 1:
	            Html_file = open(title + "1.html", "w")
	            mid += next_page_entry1.replace("next_page_link", title + "2.html")
            else:
	            curr_page_link = title + str(page_num) + ".html"				
	            next_page_link = title + str(page_num+1) + ".html"
	            if page_num == 2:
		            prev_page_link = title + "1.html"
	            else:
		            prev_page_link = title + str(page_num-1) + ".html"
	            if page_num == mid_num:
		            mid_temp = next_page_entry3.replace("next_page_link", next_page_link)
	            else:
		            mid_temp = next_page_entry2.replace("next_page_link", next_page_link)
	            mid += mid_temp.replace("prev_page_link", prev_page_link)
	            Html_file = open(curr_page_link, "w")
		            
            html_str = html_start_str + mid + html_end_str
            Html_file.write(html_str)
            Html_file.close()

################################################################################################################

# Create thumbnails for images
# note: no handling for .gifs yet. maybe not even pngs, need to test
def create_thumbnails(in_dir, out_dir=None, tn_name_extra="", size=(128, 128)):
    if in_dir == None:
        in_dir = ""
    else:
        if in_dir[-1] != "/":
            in_dir += "/"
    if out_dir == None:
        out_dir = ""
    else:
        if out_dir[-1] != "/":
            out_dir += "/"     
    img_arr = imgs_in_dir(in_dir, extensions = ("*.png","*.jpg","*.jpeg","*.JPG",)) 
    for fn in img_arr:
        f, ext = os.path.splitext(fn)
        thumbnail_dir = out_dir + f + tn_name_extra + ext
        if not os.path.isfile(thumbnail_dir):
            im = Image.open(in_dir + fn)
            im.thumbnail(size)
            im.save(thumbnail_dir, "JPEG")

thumbnail_dir = 'images/thumbnail/'
images_dir = "images/"
# Add thumbnails
create_thumbnails(images_dir, thumbnail_dir, size=(500, 500))
# Remove thumbnails that are no longer in images dir
thumbnail_arr = imgs_in_dir(thumbnail_dir)
for infile in thumbnail_arr:
    if not os.path.isfile(images_dir + "/" + os.path.basename(infile)):
        os.remove(thumbnail_dir + infile) 

################################################################################################################

# Fetch the data

with open('data.csv', "r+", newline='') as data:
    # Clear data.csv
    data.truncate(0)	
    # write data columns
    writer = csv.writer(data, quoting=csv.QUOTE_ALL)
    writer.writerow(['Date','Type','File-name','Text'])
    ##### Images #####
    #set path of images directory
    #newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
    #newpath += 'images/'
    #get list of image file names from directory
    img_arr = imgs_in_dir('images/')
    # pattern = 'images/*.jpg'
    # img_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
    for img in img_arr:
        img_ext = img[-4:].lower()
        if img_ext == ".jpg" or img_ext == ".jpeg": 
            # Get EXIF metadata from image
            im = Image.open("images/" + img)
            if im.info.get("exif") is None:
                exif_ifd = {}
                exif_dict = {"Exif": exif_ifd}
    #            exif_bytes = piexif.dump(exif_dict)
    #            piexif.insert(exif_bytes, "images/" + img)
            else:
                exif_dict = piexif.load(im.info.get("exif"))
            # Get datetime from EXIF
            dt_exif = exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal)
            if dt_exif is None:
                # get datetime EXIF from filename instead (old method)
                img_no_ext = os.path.splitext(img)[0]
                dt = datetime.strptime(img_no_ext, '%Y%m%d%H%M')
                dt_str = datetime.strftime(dt, '%Y.%m.%d %I:%M %p')
                # go ahead and insert datetime into the image EXIF
                exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = datetime.strftime(dt, u'%Y:%m:%d %H:%M:%S')
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, "images/" + img)
            else:
                # EXIF data contains datetime info
                if type(dt_exif) is bytes:
                    dt_exif = dt_exif.decode("utf-8").strip('\x00')
                dt = datetime.strptime(dt_exif, '%Y:%m:%d %H:%M:%S')
                dt_str = datetime.strftime(dt, '%Y.%m.%d %I:%M %p')
            # Get UserComment from EXIF
            # UserComment is being used for the image caption
            # I use Shotwell to add these user comments / captions
            if (exif_dict["0th"] and piexif.ImageIFD.ImageDescription in exif_dict["0th"]):
                print(exif_dict["0th"][piexif.ImageIFD.ImageDescription])
                exif_dict["Exif"][piexif.ExifIFD.UserComment] = exif_dict["0th"][piexif.ImageIFD.ImageDescription]
            user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
            if type(user_comment) is bytes:
                user_comment = user_comment.decode("utf-8").strip('\x00')
            print(img)
            if user_comment and ("OLYMPUS DIGITAL CAMERA" in user_comment or "Maker:" in user_comment):
                user_comment = ""
        else:
            # .png and .gifs (for now)
            print(img)
            img_no_ext = os.path.splitext(img)[0]
            dt = datetime.strptime(img_no_ext, '%Y%m%d%H%M')
            dt_str = datetime.strftime(dt, '%Y.%m.%d %I:%M %p')
            user_comment = ""
        writer.writerow([dt_str, "image", img, user_comment])

	##### squawks #####
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
		    writer.writerow([dt_str, "text", sqk, sqk_txt])

# sort the data by date
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

################################################################################################################

# HTML templates

html_start = """---
title: id_text
tags: id_text
---
    """
# home logo is commented out here
#html_top_scroll = """
#	<div class="top">
#<!--		<a href="../index.html"><img class="logo home" src="home_logo.png"/> </a> -->
#	</div>
#"""
# html_top_scroll = """
# 	<div class="top">
# 		<a href="../index.html"><img class="logo home" src="home_logo.png"/> </a>
# 		<a href="images.html"><img class="logo home" src="images_logo_white.png"/> </a>
# 	</div>
# """
# html_top_image = """
# 	<div class="top">
#        <a href="../index.html"><img class="logo home" src="home_logo.png"/></a>
#        <a href="scroll.html"><img class="logo home" src="images_logo.png"/> </a>
#    </div>
# """

# html_top_squawk = """
# 	<div class="top">
#                <a href="../index.html"><img class="logo home" src="squawk_logo.png"/> </a>
#        </div>
# """

html_image_entry_temp = """
	<tr>
		<td class="date"><time>date_text</time></td>
		<td class="image">
            <a href="img_src"><img src="thumbnail_src"></a>
            caption
        </td>
	</tr>
"""
html_squawk_entry_temp = """
        <tr>
		<td class="date"><time>date_text</a></time></td>
 		<td class="text">
             text_text
        </td>
        </tr>
    """

html_end = """
"""

## below (currently commented out) is alternative for above. havn't made up mind yet
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

content_id = "content"
html_start_scroll = html_start.replace("the_title", "scroll")
html_start_scroll = html_start_scroll.replace("id_text", content_id)
# html_start_scroll = html_start_scroll.replace("<top></top>", html_top_scroll)

txt_id = "text"
html_start_squawk = html_start.replace("the_title", "text")
html_start_squawk = html_start_squawk.replace("id_text", txt_id)
# html_start_squawk = html_start_squawk.replace("<top></top>", html_top_squawk)

img_id = "images"
html_start_image = html_start.replace("the_title", "images")
html_start_image = html_start_image.replace("id_text", img_id)
# html_start_image = html_start_image.replace("<top></top>", html_top_image)

################################################################################################################

# Create HTML files with templates and fetched data

pattern = '*.html'
f_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
for f in f_arr:
	print(f)
	os.remove(f)

with open('data.csv', "r+", newline='') as data:
    reader = csv.reader(data)
    scroll_mid = ""
    squawk_mid = ""
    image_mid = ""
    loops_thresh = 300
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
            caption = ""
            if row[3]:
                caption = "<figcaption>" + row[3] + "</figcaption>"
            img_dir = "/content/images/" + file_name
            thumbnail_dir = "/content/images/thumbnail/" + file_name
            image_entry = html_image_entry_temp.replace("img_src", img_dir)
            image_entry = image_entry.replace("thumbnail_src", thumbnail_dir)
            image_entry = image_entry.replace("date_text", date)
            image_entry = image_entry.replace("caption", caption)
            scroll_mid += image_entry
            image_mid += image_entry
            scroll_loop_count += 10
            image_loop_count += 10
        elif elem_type == "text":
            text = row[3]
            file_dir = "squawk/" + file_name
            squawk_entry = html_squawk_entry_temp.replace("text_page", file_dir)
            squawk_entry = squawk_entry.replace("date_text", date)
            squawk_entry = squawk_entry.replace("text_text", text)
            scroll_mid += squawk_entry
            squawk_mid += squawk_entry
            scroll_loop_count += 1
            squawk_loop_count += 1
		
            if scroll_loop_count >= loops_thresh:
                scroll_loop_count = 0
                scroll_mid = r'<table class="index content">' + "\n" + scroll_mid + "</table>\n"
                mid_pages_arr.append(scroll_mid)
                scroll_mid = ""
            if image_loop_count >= loops_thresh:
                image_loop_count = 0
                image_mid = r'<table class="index ' + img_id + r'">' + "\n" + image_mid + "</table>\n"
                mid_pages_imgs_arr.append(image_mid)	
                image_mid = ""	
            if squawk_loop_count >= loops_thresh:
                squawk_loop_count = 0
                squawk_mid = r'<table class="index ' + txt_id + r'">' + "\n" + squawk_mid + "</table>\n"
                mid_pages_sqwk_arr.append(squawk_mid)
                squawk_mid = ""
    mid_pages_arr.append(r'<table class="index content">' + "\n" + scroll_mid + "</table>\n")
    mid_pages_sqwk_arr.append(r'<table class="index ' + txt_id + r'">' + "\n" + squawk_mid + "</table>\n")
    mid_pages_imgs_arr.append(r'<table class="index ' + img_id + r'">' + "\n" + image_mid + "</table>\n")
    build_html_pages(html_start_scroll, mid_pages_arr, html_end, "scroll")
    build_html_pages(html_start_image, mid_pages_imgs_arr, html_end, img_id)
    build_html_pages(html_start_squawk, mid_pages_sqwk_arr, html_end, txt_id)

################################################################################################################
