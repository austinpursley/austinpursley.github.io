import json
import os
#run this to update HTML page
with open('data.json', "r+") as data_file:
    data = json.load(data_file)

    for i in data['set']:
        # Update directories according to JSON data.
        newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
        newpath += i['id']
        # thought: prompt user, ask if they would like to add some photos here.
        # Update JSON data, img_array, according to imgages in directory.
        i['img_array'] = os.listdir(newpath)
        i['href'] = i['id'] + '.html'

    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()