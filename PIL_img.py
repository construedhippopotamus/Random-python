# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:20:05 2018

@author: Pizzagirl

testing out PIL image tools
https://pillow.readthedocs.io/en/5.0.0/handbook/tutorial.html

python 3.6
PIL version 5.0
"""

import PIL
from PIL import ImageFilter
import os
import numpy as np

imgfile = r'C:\ProgramData\Anaconda2\envs\py36\Lib\site-packages\pytesseract\europe.jpg'
imgfile2 = r'C:\ProgramData\Anaconda2\envs\py36\Lib\site-packages\pytesseract\hawaii1.jpg'

im = PIL.Image.open(imgfile)
im2 = PIL.Image.open(imgfile2)

print("im", im)

print("\n")

print("im2", im2)

aa = np.array(im)
bb = np.array(im2)

cc = aa - bb
dd = PIL.Image.fromarray(cc)
dd.show()
dd.save(r'C:\Users\Pizzagirl\Pictures\CREATED\wed1.jpg')

#image information
#print(im)

"""
#convert files to jpeg
#for infile in imgfile:  #include all but call to python program
f, e = os.path.splitext(imgfile)
outfile = f + ".png"
print(outfile)
#make sure file not overwritten
if imgfile != outfile:
    try:
        PIL.Image.open(imgfile).save(outfile)
        
        print("Converted", outfile)
    except IOError:
        print("Cannot convert")
"""

outfile = r'C:\python36scripts\IMG_TEST\cropout.jpg'
"""
#test color changes
im = PIL.Image.open(imgfile)
#split image into individual bands
r, g, b = im.split()
im = PIL.Image.merge('RGB', (g, r, b))
im.show()
"""

#remove noise by taking median of adjacent pixels
zz = im.filter(PIL.ImageFilter.MedianFilter)
zz.show()
zz = im.filter(PIL.ImageFilter.GaussianBlur)
#zz.show()
zz = im.filter(PIL.ImageFilter.UnsharpMask)
zz.show()
#cropped = PIL.Image.fromarray(a)
#cropped.show()
#print(cropped)
#print(a)
#print("\n")
#print(a[:0,:,:])
#print("\n")

"""
#get rid of color channel(s)
#image is a list of color values. Each color value is (R, G, B)
a = np.array(im)
#multiply all R by 0 --> [0, G, B] --> first col is zero
a[:,:,0] *=0
#multiply all G by zero. (second col)
a[:,:,1] *=0
a = PIL.Image.fromarray(a)
a.show()
"""

"""
#copying a subrectangle and pasting it back in
box = (600, 600, 1400, 1400)
region = im.crop(box)
#region.show()  

region = region.transpose(PIL.Image.ROTATE_180)
im.paste(region, box)
im.show()
"""


"""
#copy image and paste overlapping (roll)
def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.show()
    return image

roll(im, 500)         
"""

"""           
#rotate image
out = im.rotate(37)
out.show()

#transpose (MIRROR)
out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
out.show()
"""

# multiply each pixel by 1.2
#out = im.point(lambda i: i + 100)

out = im.filter(ImageFilter.FIND_EDGES)

#out.show()

#next: how to extract text (OCR)? eqn for this?
#look at PILLOW source code - does it already use gpu?
#how to extract storm drain lines?

            