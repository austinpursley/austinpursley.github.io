import json
import os

# Update JSON data, img_array, according to imgages in directory.
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
        img_array = os.listdir(newpath)
        img_array.reverse()
        i['img_array'] = img_array

    #get img list from directory of images
    img_array = os.listdir(newpath)
    #reverse it so that order is new to old
    img_array.reverse()
    #update json according to directory
    data['img_array'] = img_array

    #go to the beginning of the file (because we loaded to end earlier)
    data_file.seek(0)
    #update json file (indent=4 >>> pretty printing)
    json.dump(data, data_file, indent=4)
    data_file.truncate()