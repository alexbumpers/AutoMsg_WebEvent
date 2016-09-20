"""
This document demonstrates reading and writing to a file using the print_function module. It is currently not in use for this project
(e.g., scraping Web Event and sending an email). It can be ignored for all intents and purposes at this time.
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2

#defines variable to open file in read mode
txt_file = open('test.txt', 'r')
#defines variable to read content of file
file_content = txt_file.read() 

#with print_function import, make sure to use parentheses around prints
print (file_content) 

txt_file.close()


new_file = open('scrapedinfo.txt', 'w') #defines variable to open new_file in write mode
nf_content = print("Hello!", file=new_file)

