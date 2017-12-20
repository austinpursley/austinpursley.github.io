import json
import os

# Update JSON data, img_array, according to imgages in directory.
with open('data.json', "r+") as data_file:
    newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
    newpath += 'images'
    print(newpath)
    data = json.load(data_file)
        # thought: prompt user, ask if they would like to add some photos here.

    #data['img_array'] = os.listdir(newpath)
    img_array = os.listdir(newpath)
    img_array.reverse()
    data['img_array'] = img_array


    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()