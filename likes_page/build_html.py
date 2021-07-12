
def build_html_pages(html_start_str, mid_pages_arr, html_end_str, title):
    """ creates HTML pages given template pieces

    :param html_start_str: start of HTML page
    :param mid_pages_arr: list where each element is middle section for a new HTML file
    :param html_end_str: end of HTML page
    "param title: what the HTML file will be named
    """
    next_page_entry1 = """
	    <tr class="nav">
		    <td style="visibility: hidden;" class="nav_button"></td>
		    <td class="nav_button"><a href="next_page_link">next page</a></td>
	    </tr>
    """
    next_page_entry2 = """
	    <tr class="nav">
		    <td class="nav_button"><a href="prev_page_link">prev page</a></td>
		    <td class="nav_button"><a href="next_page_link">next page</a></td>
	    </tr>
	    """
    next_page_entry3 = """
	    <tr class="nav">
		    <td class="nav_button"><a href="prev_page_link">prev page</a></td>
		    <td style="visibility: hidden;" class="nav_button"></td>
	    </tr>
    """
    mid_num = len(mid_pages_arr)
    if mid_num == 1:
        #case where only writing one HTML page
        html_str = html_start_str + mid_pages_arr[0] + html_end_str
        Html_file = open(title + ".html", "w")
        Html_file.write(html_str)
        Html_file.close()	
    else:
        #writing two or more HTML pages
        for page_num, mid in enumerate(mid_pages_arr, 1):
            if page_num == 1:
	            Html_file = open(title + ".html", "w")
	            mid += next_page_entry1.replace("next_page_link", title + "2.html")
            else:
	            curr_page_link = title + str(page_num) + ".html"				
	            next_page_link = title + str(page_num+1) + ".html"
	            if page_num == 2:
		            prev_page_link = title + ".html"
	            else:
		            prev_page_link = title + str(page_num-1) + ".html"
	            if page_num == mid_num:
		            mid_temp = next_page_entry3.replace("next_page_link", next_page_link)
	            else:
		            mid_temp = next_page_entry2.replace("next_page_link", next_page_link)
	            mid += mid_temp.replace("prev_page_link", prev_page_link)
	            Html_file = open(curr_page_link, "w")
		            
            html_str = html_start_str + mid + html_end_str
            Html_file.write(html_str)
            Html_file.close()
