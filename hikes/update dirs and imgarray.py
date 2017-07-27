import json
import os

with open('hiking_data.json', 'r+') as data_file:
	
    data = json.load(data_file)
    for i in data['hiking_places']:
		## Update directories according to JSON data.
        newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
        print(newpath)
        newpath += i['id']
        if not os.path.exists(newpath):
            os.makedirs(newpath)
			##thought: prompt user, ask if they would like to add some photos here.
		## Update JSON data, img_array, according to imgages in directory.
        i['img_array'] = os.listdir(newpath)
    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()
        
