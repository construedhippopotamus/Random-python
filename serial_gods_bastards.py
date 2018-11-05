# -*- coding: utf-8 -*-
"""
Web scraping: download all chapters of The Gods Are Bastards web serial.

python 3.6
"""
#import beautifulsoup4 as bs4
from bs4 import BeautifulSoup
import requests
import re
from pathlib import Path

base_url = r'https://tiraas.net/table-of-contents/'

def get_url(base_url):
    
    r = requests.get(base_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'lxml')
    
    regex = 'https://tiraas.wordpress.com/20.'
    
    url_list = []
    
    for li in soup.findAll('li'):
        
        try:
            link = li.a.get('href')
            #print("link", link)
            m = re.search(regex, link)
        
            if m is None:
                pass
            else:
                #print(link)
                url_list.append(link)
        except: NameError
    
    return url_list

#download all links
def download_page(url_list):
    for url in url_list:
        r2  = requests.get(url)
        folder = Path(r"C:\Users\Pizzagirl\Documents\programming\python\web scraping\pages")
    
        name = url.split('/')[-2] + '.html'
        print(url, name) 
        filename = Path(folder, name)
        f = open(filename, 'wb')
        f.write(r2.content)
        f.close
        #print("\n closed")
    return

url_list = get_url(base_url)
download_page(url_list)
print("\n  done")