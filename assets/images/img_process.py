from PIL import Image
import glob
from pathlib import Path
import shutil
import math

img_types = ("*.jpg","*.JPG","*.jpeg", "*.png", "*.gif")
in_dir = "raw_images/"
out_dir = "./"
img_arr = [f for f_ in [glob.glob(in_dir + e) for e in img_types] for f in f_]

max_pixels = 500000

for fn in img_arr:
    im = Image.open(fn)
    width, height = im.size
    pixel_cnt = width * height
    if pixel_cnt > max_pixels:
        scale = math.sqrt(max_pixels/pixel_cnt)
        im = im.resize((int(width*scale), int(height*scale)))
    # if Path(fn).suffix  == ".png":
    #     im.save(out_dir + Path(fn).stem + ".webp", quality=80)
    if Path(fn).suffix != ".gif":
        im.save(out_dir + Path(fn).stem + ".webp", quality=90)
        # im.save(out_dir + Path(fn).name, optimize=True)
    else:
        # just copy gifs and PNGS for now (Pillow not saving as expected)
        shutil.copyfile(fn, out_dir + Path(fn).name)