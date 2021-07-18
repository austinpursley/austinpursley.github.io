# i didn't check which of these are necessary or not
import os
import glob
from datetime import datetime
import re
from bs4 import BeautifulSoup
from PIL import Image
import piexif
import piexif.helper

#just copy & pasting code relics / scratch here for now
#eventually could make tool to make editing EXIF image metadata easier for this page
pattern = 'images/*.jpg'
img_arr = sorted((os.path.basename(x) for x in glob.glob(pattern)), reverse=True)
    for img in img_arr:

#        for tag in exif_dict["Exif"]:
#            print(piexif.TAGS["Exif"][tag]["name"], exif_dict["Exif"][tag])
        
#        img_no_ext = os.path.splitext(img)[0]
#        # date should be encoded within file name
#        dt = datetime.strptime(img_no_ext, '%Y%m%d%H%M')
#        dt_str = datetime.strftime(dt, '%Y:%m:%d %H:%M:00')
#        image = Image.open("images/" + img)
#        exif_ifd = {piexif.ExifIFD.DateTimeOriginal: dt_str}
#        exif_dict = {"Exif": exif_ifd}
#        exif_bytes =piexif.dump(exif_dict)
#        image.save("images/" + img, subsampling=0, quality=90, exif=exif_bytes)

#        dt_str = datetime.strftime(dt, '%Y:%m:%d %H:%M:00')
#        image = Image.open("images/" + img)
#        exif_ifd = {piexif.ExifIFD.DateTimeOriginal: dt_str}
#        exif_dict = {"Exif": exif_ifd}
#        exif_bytes =piexif.dump(exif_dict)
#        image.save("images/" + img, subsampling=0, quality=90, exif=exif_bytes)

        # CODE BELOW SAVES IMAGES WITHOUT EXIF DATA
        # ****** JUST A HACK, NOT RECOMMENDED *************
        # ****** JPEGS WILL BE SAVED AGAIN AND LOSE INFO **********
#        image = Image.open("images/" + img)
#        data = list(image.getdata())
#        image_without_exif = Image.new(image.mode, image.size)
#        image_without_exif.putdata(data)
#        image_without_exif.save("images/" + img, subsampling=0, quality=90)
