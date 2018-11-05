# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:13:16 2017

@author: Jenny

Download all episodes of Coffee Break French on a webpage.
"""
import shutil
import requests
from bs4 import BeautifulSoup
import os


URL = "https://radiolingua.com/tag/cbf-season-2/page/3/"

def get_link1():
     
    # create response object
    r = requests.get(URL)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'lxml')
     
    # find all "continue reading" links on web-page
    #linkclass =  soup.findAll('p', attrs={'class' : 'continue-reading'})
    
    linklist=[]
    
    #links to next page
    for pclass in soup.findAll('p', attrs={'class' : 'continue-reading'}):
        links = pclass.findAll('a')[0].attrs['href']
        linklist.append(links)
        
    return linklist


def open_pages(linklist):
    
    mp3list=[]
    
    for link in linklist:
        r1=requests.get(link)
        soup1 = BeautifulSoup(r1.content, 'lxml')        
        URL2 = soup1.findAll('a')                
        mp3links = [ page['href'] for page in URL2 if page['href'].endswith('mp3')]
        mp3list.append(mp3links[0])    
        
    return mp3list

def dnload(mp3list):

    for song in mp3list:
        r2= requests.get(song, stream= True)
        loc_file_name = os.path.join('C:\Users\Pizzagirl\Documents\French', song.split('/')[-1] ) 

        with open(loc_file_name, 'wb') as f:
            shutil.copyfileobj(r2.raw, f)
    return #loc_file_name       


if __name__ == "__main__":
 
    # getting all video links
    video_links = get_link1()
 
    # download all videos
    dnlist = open_pages(video_links)
    
    dnload(dnlist)
    
    print "done"
