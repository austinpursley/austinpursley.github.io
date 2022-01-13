import csv
import os
import glob
from datetime import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
import piexif
import piexif.helper

def imgs_in_dir(in_dir):
    extensions = ("*.png","*.jpg","*.jpeg","*.JPG",)
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
    mid_num = len(mid_pages_arr)
    print(mid_num)
    if mid_num == 1:
        #case where only writing one HTML page
        html_str = html_start_str + mid_pages_arr[0] + html_end_str
        Html_file = open(title + ".html", "w")
        Html_file.write(html_str)
        Html_file.close()	
    else:
        #writing two or more HTML pages
        for page_num, mid in enumerate(mid_pages_arr, 1):
            if page_num == 1:
	            Html_file = open(title + ".html", "w")
	            mid += next_page_entry1.replace("next_page_link", title + "2.html")
            else:
	            curr_page_link = title + str(page_num) + ".html"				
	            next_page_link = title + str(page_num+1) + ".html"
	            if page_num == 2:
		            prev_page_link = title + ".html"
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
    img_arr = imgs_in_dir(in_dir) 
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
        user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
        if type(user_comment) is bytes:
            user_comment = user_comment.decode("utf-8").strip('\x00')
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

html_start = """
    <!DOCTYPE html>
    <html>

    <head>
        <title> the_title </title>
        <link rel="stylesheet" href="../style.css">
        <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 850px)" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    </head>

    <body id="id_text">
    <top></top>
        <table>
    """

html_top_scroll = """
	<div class="top">
<!--		<a href="../index.html"><img class="logo home" src="home_logo.png"/> </a> -->
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

html_image_entry_temp = """
	<tr class="content">
		<td class="date"><time>date_text</time></td>
		<td class="image"><a href="img_src"><img src="thumbnail_src"></a><p>caption</p></td>
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
            caption = row[3]
            img_dir = "images/" + file_name
            thumbnail_dir = "images/thumbnail/" + file_name
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

################################################################################################################
