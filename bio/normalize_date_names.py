import os
text_path = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.dirname(os.path.realpath(__file__)) + '/image_name_fix'
file_list = os.listdir(img_path)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for file in file_list:
    f_list = os.path.splitext(file)
    if (f_list[1] == ".jpg"):
        f = f_list[0]
        date = f[:15]
        if (is_number(date) == True):
            newdate = (date[:4] + "." + date[4:6] + "." + date[6:8] +
                       date[8:11] + "." + date[11:13] + "." + date[13:15])
            os.rename(text_path + "/image_name_fix/" + file, text_path +
                      "/image_name_fix/" + newdate + ".jpg")

