# -*- coding: utf-8 -*-
"""
script to download all solutions from a given w3 schools practice 
problem page.

python 3.6
"""
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re  #regex
from pathlib import Path


#get solution page links    
def ex_links(main_page):
    
    # create response object
    r = requests.get(main_page)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'lxml')
    
    #list to store links to solution pages
    sln_list = []
    
    #get solution hefs that contain 'exercise-'
    #this also works:  soup.select('a[href*="exercise-"]')
    for alink in soup.findAll(href=re.compile('exercise-')):  
        #alink is bs4.element.Tag. need to extract the 'href' attribute.
        sln_href_short = alink['href']
        
        #print(sln_href_short)
        sln_list.append(sln_href_short)
    return sln_list

#write solution pages to disc
def save_sln(sln_link_list, base_url, save_path):
    
    for sln_pg in sln_link_list:

        #full-length href 
        sln_href = base_url + sln_pg
        #print(sln_href)
    
        # create response object
        r = requests.get(sln_href)
        
        #create file name
        file_name = sln_pg.replace('.php', '')
        #print(file_name)
        
        file = Path(save_path, file_name + '.html')
           
        #write to file - this will overwrite any of same name
        with open(file, 'wb') as f:
            f.write(r.content)

#page to start scraping from
main_page = r'https://www.w3resource.com/python-exercises/web-scraping/index.php'

#first part of solution href (links in html are relative)
base_url = "https://www.w3resource.com/python-exercises/web-scraping/"

#full path to where the files should be saved
save_path = r'C:\Users\Pizzagirl\Documents\programming\python\web scraping\w3_scrape_slns'



#call functions
save_sln(ex_links(main_page), base_url, save_path)

