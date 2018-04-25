# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:50:36 2018

@author: Pizzagirl

add all same-dimensioned images in folder to each other (2 at a time) to find cool combinations

python 3.6
PIL 5.0
"""

import PIL
import os
import numpy as np
import time

start_time = time.time()

#location of images to combine
imgfldr = r'C:\Users\Pizzagirl\Pictures\CREATED\combine'
#save location of created images
savefldr = r'C:\Users\Pizzagirl\Pictures\CREATED'

os.chdir(imgfldr)
files = os.listdir(imgfldr)


#iterate through all images
for img in range(0,10):

    try:
        im = PIL.Image.open(files[img])
    except IOError:
        pass
    else:
        imarr = np.array(im)
    
    for addimg in range(0,10):
        if files[addimg] == files[img]:
            pass
        else:  #add images
            try:
                im2 = PIL.Image.open(files[addimg])
            except IOError:
                pass
            else:
                imarr2 = np.array(im2)
                try:
                    minus = imarr + imarr2
                except ValueError:
                    pass
                else:
                    res = PIL.Image.fromarray(minus)
                    name1 = os.path.splitext(files[img])[0]
                    name2 = os.path.splitext(files[addimg])[0]
                    filename = name1 + "_" + name2 + ".jpg"

                    saveloc = os.path.join(savefldr, filename)
                    res.save(saveloc)

            
print("--- %s seconds ---" % (time.time() - start_time))
print("%s files" %len(files))

