from update_html import update_html
from update_data import update_data

ask_if_new = input("add new question? enter y for yes ")
if ask_if_new == 'y':
    update_data()
else:
    print('not adding new question')

update_html()