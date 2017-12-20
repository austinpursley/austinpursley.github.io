import json
import os
#run this to update HTML page
with open('data.json', "r+") as data_file:
    data = json.load(data_file)

    for i in data['set']:
        # Update directories according to JSON data.
        newpath = os.path.dirname(os.path.realpath(__file__)) + '/'
        #new path is directory of images
        newpath += i['id']
        #href of images href
        #i['href'] = i['id'] + '.html'
        # JSON img_array is equal to list of images in image directory
        i['img_array'] = os.listdir(newpath)


    data_file.seek(0)
    json.dump(data, data_file, indent=4)
    data_file.truncate()