import json
import os
import glob

# Update JSON data, img_array, according to images in directory.
with open('data.json', "r+") as data_file:
    newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
    newpath += 'images'
    print(newpath)
    data = json.load(data_file)
        # thought: prompt user, ask if they would like to add some photos here.

    for i in data['set']:
        # Update directories according to JSON data.
        newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
        #new path is directory of images
        newpath += i['id']
        #href of images href
        #i['href'] = i['id'] + '.html'
        # JSON img_array is equal to list of images in image directory
        # This function gets list of image file names from the images folder
        pattern = "images/*.jpg"
        img_array = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
        i['img_array'] = img_array

    #go to the beginning of the file (because we loaded to end earlier)
    data_file.seek(0)
    #update json file (indent=4 >>> pretty printing)
    json.dump(data, data_file, indent=4)
    data_file.truncate()

html_gal_start = """
<!DOCTYPE html>
<html>
<head>
	<link href="img_gal_style.css" rel="stylesheet">
	<link href="../style.css" rel="stylesheet">
	<link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 850px) and (min-aspect-ratio: 1/1)" />
	<link rel="stylesheet" href="../mobile_portrait.css" media="screen and (max-device-width: 500px)" />
	<link rel="stylesheet" href="../mobile_portrait.css" media="screen and (max-device-width: 1200px) and (max-aspect-ratio: 1/1)" />
</head>


<body id="img_gal">
	<div class="top">
	   <div class="logo home-icon">
                   <!-- <a href="../index.html"> <img src="home_logo_images.png"/> </a> -->
		   <a href="../home.html"> <img src="home_logo_images.png"/> </a>
	   </div>
	   <div class="logo secondary-icon">
		   <a href="img_carousel.html"><img src="img_carousel_logo.png"/> </a>
	   </div>
	</div>
	
	<div id="lightbox_temp_area"></div>
	
	<div id="content_area">
"""
html_gal_mid_temp = """
	<a class="lightbox" href="#IMG_NAME"><img id="IMG_NAMEanchor" src="thumbnails/IMG_NAME"/></a>
"""

html_gal_mid_temp2 = """
	<div class="lightbox-target" id="IMG_NAME">
	   <img src="images/IMG_NAME"/>
	   <a class="lightbox-close" href="#IMG_NAMEanchor"></a>
	</div>
"""

html_gal_end = """
</body>
</html>
"""

# update img gallery index
index_mid = ""
for fn in img_array:
    index_mid_part = html_gal_mid_temp.replace("IMG_NAME", fn)
    index_mid += index_mid_part

index_mid += """
	</div>
"""

for fn in img_array:
    index_mid_part = html_gal_mid_temp2.replace("IMG_NAME", fn)
    index_mid += index_mid_part

html_str = html_gal_start + index_mid + html_gal_end
Html_file = open("img_gal.html", "w")
Html_file.write(html_str)
Html_file.close()

html_carousel = """
<!DOCTYPE html>
<html>
<head> 
	<title> Images </title>
	<link rel="stylesheet" href="../style.css">
	<link id="img_style" rel="stylesheet" href = "../wide_win_img_style.css">

    <!-- js libraries -->
	<script src="../jquery.min.js"></script>
    <!-- My js -->
	<script src="../img_carousel.js" defer></script>
</head>
<body id="img_carousel">

	<div class="top">
	   <div class="logo home-icon">
		   <!-- <a href="../index.html"> <img src="home_logo_images.png"/> </a> -->
                   <a href="../home.html"> <img src="home_logo_images.png"/> </a>
	   </div>
	   <div class="logo secondary-icon">
		   <a href="img_gal.html"><img src="img_gallery_logo.png"/> </a>
	   </div>
	</div>
	
	<div id="id">images</div>
	
	<div id="slideshow">
		<img src="images/FIRST_IMG" alt="start" id="img_click_change" />
	</div>
	
	<div id="nxt_pre_bttns">
		<button class="previous">&#8249;</button>
		<button class="next">&#8250;</button>
	</div>
	
</body>
</html>
"""

html_str = html_carousel.replace("FIRST_IMG", img_array[0])
Html_file = open("img_carousel.html", "w")
Html_file.write(html_str)
Html_file.close()

# move thumbnails for any removed images
# want to keep them in case decide want to put images back
# could one day make thumbnails with images (gimp+python?)_
pattern = "thumbnails/*.jpg"
thumb_array = glob.glob(pattern)
for tn in thumb_array:
    bn = os.path.basename(tn)
    if bn not in img_array:
        os.rename(tn, "removed/thumbnails/" + bn)
