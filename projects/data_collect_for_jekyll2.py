#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:11:47 2022

@author: austinpursley
"""

import glob
import markdownify
from bs4 import BeautifulSoup
from pathlib import Path
import re

mydir=""
html_list = sorted(glob.glob(r"[0-9][0-9]_*.html"))


for fn in html_list:
    with open(fn, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, features="html.parser")
        title = "\"" + soup.h1.text + "\""
        soup.h1.extract()
        front_matter = """---
layout: post
title: _TITLE_
tags: project
---
""".replace("_TITLE_", title)
        content = soup.find(id='content_area').extract()
        html = "".join([str(item) for item in content.contents])
        # date = re.findall(r'(\d{1,2}.\d{1,2}.\d{4})|(\d{4}-\d{1,2}-\d{1,2}.)', html)[0]
        dg1 = re.search(r"(\d{1,2}).(\d{1,2}).(\d{4})", html)
        dg2 = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", html)
        
        if dg1:
            html = html.replace(dg1[0],"")
            date = dg1.group(3) + "-" + dg1.group(1).zfill(2) + "-" + dg1.group(2).zfill(2)
        elif dg2:
            html = html.replace(dg2[0],"")
            date = dg2.group(1) + "-" + dg2.group(2).zfill(2) + "-" + dg2.group(3).zfill(2)
        else:
            print('error no date found')
            exit
        html = BeautifulSoup(html, "html.parser").prettify()
        # convert html to markdown
        h = markdownify.markdownify(html, heading_style="ATX")
        h = front_matter + h
        h = h.replace("# \n", "#")
        h = h.replace(r"images/", r"/assets/images/")
        syn_hl_chng = re.finditer("(```)(.*?)(```)", h, flags=re.DOTALL)
        if syn_hl_chng:
            for m in syn_hl_chng:
                h = h.replace(m.group(0), "{% highlight python linenos %}" + m.group(2) + "{% endhighlight %}")
        with open(mydir+date+"-proj-"+Path(fn).stem[3:] + ".md", "w") as md_file:
            md_file.write(h)