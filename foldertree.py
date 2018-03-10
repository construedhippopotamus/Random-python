# -*- coding: utf-8 -*-
"""
foldertree.py

Created on Wed Mar 07 19:34:48 2018

#create nested folder structure specified in text input file.
#duplication/overwriting of folders does not occur.
#python 2.7
#Author = Jenny Mital 3/7/2018

"""

import os
import csv
import sys

#list of folders to be created, tab delimited, in the format of one folder name per line.
#subfolders are on each subsequent lines, with a tab to denote how many levels from base folder.

txtdoc= r'C:\Users\Pizzagirl\Documents\programming\testfolder\folders.txt'

#place new folders here
path1 = r'C:\Users\Pizzagirl\Documents\programming\testfolder'

#user input from cmd - overrules above if given

print('Program to create nested folder tree from text file list of folders. No folder overwriting. \n')
loc = str(raw_input(r'Select location of text file with folder names. Enter D to use default location. Enter N to input new location: '))
if loc == 'D':
    txtdoc= r'C:\Users\Pizzagirl\Documents\programming\testfolder\folders.txt'
elif loc == 'N':
    txtdoc = str(raw_input(r'Enter path and name of txt file (format: C:\folder\text.txt ): '))
else:  #other character or no character
    print("Incorrect input. Quitting program.")
    sys.exit()
    
loc2 = str(raw_input(r'Select location to create new folders. Enter D to use default location. Enter N to input new location: '))
if loc2 == 'D':
    path1= r'C:\Users\Pizzagirl\Documents\programming\testfolder'
elif loc2 == 'N':
    path1 = str(raw_input(r'Enter path and name of txt file (format: C:\folder ): '))
else:  #other character or no character
    print("Incorrect input. Quitting program.")
    sys.exit()


pathlist = []
j= -2  #path record variable

with open(txtdoc, 'r') as f:
    csvreader = csv.reader(f, dialect='excel-tab')
    #csvreader = csv.reader(f, delimiter=',')
    for line in csvreader:
        
        i=0
        
        while i < len(line):
                                
            if len(line)>0:  #exclude blank lines
                
                if len(line[i])>0:  #has content - exclude blank spaces
                    #print("line[i]", line[i])
                        
                    if i <= j: #new upper level directory
                        #go up 1 or more directories. Number to go up = j - i

                        count = i
                        #print("count", count, "j", j)
                        while count <= j:

                            path1, folder = os.path.split(path1)
                            #print("path1", path1, "folder", folder)
                            count += 1
                            #print ("inside while", path1)
                        
                        
                        path1 = os.path.join(path1, line[i])
                        #print("outside while", path1)
                        #print("exit loop, -")
                    #print ("outside if", path1)
                        
                    if i > j:  #subdirectory
                        path1 = os.path.join(path1, line[i])
                        #print('++')

                    #print("final", path1)
                    j=i  #record i that had content  
                    pathlist.append(path1)                                           
                        
            i+=1
            
#print (pathlist)
path1 = r'C:\Users\Pizzagirl\Documents\programming\testfolder'
outfile = os.path.join(path1, 'pathout.txt')

with open(outfile, 'w') as ff:
    #write paths to text file
    for path1 in pathlist:
        ff.write(path1)
        ff.write("\n")

#status counters
created = 0
nocreate = []

#create folder for each path
for path1 in pathlist:
    try:
        os.makedirs(path1)
        created +=1
    except WindowsError:  #if path already exists do not create
        nocreate.append(path1)

print("{} folders created").format(created)   
    
    
