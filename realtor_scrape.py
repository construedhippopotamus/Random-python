# -*- coding: utf-8 -*-
"""

Scrape Knoxville realtor database - practice from upwork

Need mechanize and/or form simulator to turn pages. Not going to do that right now.

Also, need to implement multiprocessing to speed this up:
    https://github.com/kadnan/olxcar/blob/master/list_parallel.py
    https://www.samueltaylor.org/articles/speed-up-web-scraping.html

python 2.7  bs4

"""
import shutil
import requests
from bs4 import BeautifulSoup
import os
import csv
import re
#import multiprocessing     #implement this to speed up the search


URL = "https://netforum.avectra.com/eweb/DynamicPage.aspx?Site=KAAR&WebCode=IndResult&FromSearchControl=Yes"


#could I do previous sibling?

#NOTE: need to do mechanize or something to "click" on the next page number -
# that is the only way to get it.
def nextpg(soup):

    next_a = soup.findAll('a', attrs={'class' : 'bodytinybold'})
    print(next_a[0].attrs)
   
    print("\n")
    #see what attributes the tag has
  
    #can put attributes in parenthesis
    #next_button = next_div[]
    #print("next button", nextbutton)

    return 


#Get links to host details on current page of results
def get_realtors():
    
    #initialize lists to hold data
    name = []
    company_list = []
    address1_list = []
    address2_list = []
    city_list = []
    state_list = []
    zip_list = []
    phone_list = []
    fax_list = []
    email_list = []

    # create response object
    r = requests.get(URL)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'lxml')

    #host description links
    for tdclass in soup.findAll('td', attrs={'class' : 'PadLeft10'}):
       
        #realtor = tdclass. works, but not needed.
        #name = tdclass.span.text 
    
        
        address = []
        address_list = []
        
        #descendants is all of tag's children and their children.
        for child in tdclass.descendants:
          
            if child.string:
                format_child = child.string.strip("\n'").encode('ascii', 'ignore')
                #remove duplicate data
                address.append(format_child)
            
        #print(address)   
        #append doesn't work in this case because of referencing that I don't understand
            address.append(address)
                                                
    print(address)
            
          
    #print(address_list)
    
    #write addresses to csv
    csv_file = r'C:\Users\Pizzagirl\Documents\programming\python\realtor_scrape.csv'
    with open(csv_file,"w") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for rowi in address_list:
            writer.writerow(rowi)
            

    return

    #can't split as string due to escape characters. Use bs4 find next or find siblings methods. read docs!


    """

    
        linkdata=requests.get(fulllink)
        souppg = BeautifulSoup(linkdata.content, 'lxml')  

        #get host title      
        pgtitle = souppg.findAll('h1')[0].text             
        #print("title", pgtitle[0].text)
        #titlelist.append(pgtitle) 

        #Host availability in July/Aug?
        Julavail = souppg.findAll('div', attrs = {'class': 'hostcalmonthinner dt2018Jul'})  
        #Augavail = souppg.findAll('div', attrs = {'class': 'hostcalmonthinner dt2018Aug'})
     
        #Minimum stay length
        minstay = souppg.findAll('p', attrs = {'class': 'text-muted'})
        minstayprint = str(minstay)
  

        myrow.append([pgtitle, Jul, minstayprint[99:], fulllink])
    
    #write to csv file
    #test which is faster: write data as I get it, or the loop below.
    #potential problems with loop below is it assumes all lists are same length. would have to inject nulls if data missing to maintain same length.
    with open('C:\Users\Pizzagirl\Documents\programming\python\realtor_scrape.csv',"w") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for rowi in myrow:
            writer.writerow(rowi)
    """

if __name__ == "__main__":
 
    # getting all host description links on current page
    host_links = get_realtors()
 
    # get host availability information from each link
    #dnlist = open_pages(host_links)
    
    print "done"
