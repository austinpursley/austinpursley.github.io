import os
import json

html_temp = """
<!DOCTYPE html>
<html>
<head> 
	<title> title2 </title>
	<link rel="stylesheet" href="../style.css">
	<link id="img_style" rel="stylesheet" href = "../wide_win_img_style.css">
	<!-- <link rel="stylesheet" href="../mobile.css" media="screen and (max-device-width: 850px) and (min-aspect-ratio: 1/1)" />
	<link rel="stylesheet" href="../mobile_portrait.css" media="screen and (max-device-width: 500px)" />
	<link rel="stylesheet" href="../mobile_portrait.css" media="screen and (max-device-width: 1200px) and (max-aspect-ratio: 1/1)" /> -->
    <!-- js libraries -->
	<script src="../jquery.min.js"></script>
    <!-- My js -->
	<script src="../img_carousel.js" defer></script>
</head>
<body id="hiking_page">
	<div class="top">
	
		<div class="home-icon logo">
			<!-- <a href="../index.html"> <img src="home_logo_hike.png"/> </a> -->
                        <a href="../home.html"> <img src="home_logo_hike.png"/> </a>
		</div>
		
		<div class="logo secondary-icon logo">
			<a href="hikes.html"> <img src="hiking_logo_back.png"/> </a>
		</div>
		
		<h1 id = "title">title2</h1>
		
		<div id="id" class="hidden">this_id</div>
		
	</div>
	<div id="slideshow">
		<img src="img_array0" alt="title2" id="img_click_change" />
	</div>
	
	<div id="nxt_pre_bttns">
		<button class="previous">&#8249;</button>
		<button class="next">&#8250;</button>
	</div>
	
</body>
</html>
"""
#json and python
#import name from json, have all files written with that name
#edit the string to respective whatever

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
        img_array0 = i["id"] + "/" + i['img_array'][0]
        title2 = i['title2']
        html_str = html_temp.replace("title2",title2)
        html_str = html_str.replace("img_array0", img_array0)
        html_str = html_str.replace("this_id", id)
        Html_file = open(file_name, "w")
        Html_file.write(html_str)
        Html_file.close()

    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()
