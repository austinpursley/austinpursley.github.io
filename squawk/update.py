import os
import csv
from update_html import update_html
from datetime import datetime
from update_data import update_data
from new_squawk import new_squawk

ask_if_new = input("add new tweet? enter y for yes ")
if ask_if_new == 'y':
  new_squawk()
else:
    print('not adding new tweet')
update_data()
update_html()
