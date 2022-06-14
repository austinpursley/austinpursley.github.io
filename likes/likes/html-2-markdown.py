#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:28:00 2022

@author: austinpursley
"""

import glob
from pathlib import Path
import re
import os
from PIL import Image
import pandas as pd
import markdownify

front_matter = """---
layout: likes-page
---
"""


html_list = sorted(glob.glob(r"*.html"))
for fn in html_list:
    with open(fn, 'r') as f:
            contents = f.read()
            md = markdownify.markdownify(contents, heading_style="ATX")
            md = front_matter + md
            with open(Path(fn).stem + ".md", "w") as md_file:
                md_file.write(md)
            # soup = BeautifulSoup(contents, features="html.parser")