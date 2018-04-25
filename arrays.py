# -*- coding: utf-8 -*-
"""
arrays.py

Created on Mon Apr  2 13:35:29 2018

@author: Pizzagirl

Practice matrix operations for image processing

"""
import numpy as np
from PIL import Image
from PIL import ImageFilter

#in numpy, matrices are 2D. arrays can be ND.
#input array

#print(arr2)
# https://en.wikipedia.org/wiki/Kernel_(image_processing)
# C:\Users\Pizzagirl\Documents\programming\python\resources\images and gpu\Kernel (image processing) - Wikipedia_files


imgfile = r'C:\ProgramData\Anaconda2\envs\py36\Lib\site-packages\pytesseract\europe.jpg'

img = Image.open(imgfile)

box = (1000, 1000, 1500, 1500)
cropped = img.crop(box)
#cropped.show()
imgarr = np.array(cropped)
print("cropped array length", len(imgarr[0]))
#len = 500; each element has R, G, B.


#define arrays

arr3 = ([
         [1,2,3],
         [4,5,6],
         [7,8,9]])

arr5 =         ([[1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5]])

idkern3 =  ([[0,0,0],[0,1,0],[0,0,0]])

idkern5 =  ([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],])
onekern5 = ([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]])

#----------------------------# 
# kernel: the matrix to multiply with the data

#function to make slice of array match kernel

print("\n")
#add zeroes to edges
def zero_pad(kernel, arr):

    #number of rows to add on
    addnum = (len(arr) - 1) // 2

    #number of elements in rows
    #rowlen = len(arr)+ 2*addnum
    zerow = []

    for row in arr:
        for ii in range(0, addnum):
            row.append(0)
            row.insert(0,0)        
    rlen = len(arr[0])
        
    for ii in range(0,rlen):
        zerow.append(0)
        
    for jj in range(0, addnum):
        arr.append(zerow)
        arr.insert(0,zerow)
        
    final = np.array(arr).reshape(9,9)
    
    return final

#padded = zero_pad(idkern5, arr5)

#print("padded arr5:", padded)

print("\n")

#----------------------------# 
# Convolution: kernel on left, array on right. kernel and comparison are of kernel MUST be same dims 
# (pad array with zeros if needed). 
# middle value of output array = sumproduct( kernel elem, R-->L, bottom--> top) * ( array elem, L-->R, top --> bottom)

# inputs are two square arrays; NOT numpy arrays.
def calcpixel(kernel, arr):
    sum = 0
    out = 0
    arri = 0
    #store filtered array
    arrout = []
    
    if len(kernel) == 1:   #1D array 
        #calculate the value of one pixel:
        for val in range(len(kernel), 0, -1):
            out = kernel[val-1] * arr[arri]

            sum = sum + out
            #print("sumflat", sum)
            arri+=1
          
    elif len(kernel) > 1:        #for array with multiple rows
        #print("len", len(kernel))
        #print("\n")
        padxstart = int((len(arr)-len(kernel))/2)   #padded array row iterator start point: first non-padded array value
        padystart = int((len(arr[0])-len(kernel[0]))/2)  #padded array column iterator start point: first non-padded array value
        #2 for both
        for padx in range(padxstart,len(arr)-padxstart):  #loop through padded array rows
            for pady in range(padystart, len(arr[0])-padystart):  # through padded array columns
                #print("arr value", arr[padx][pady])
                for kernx in range(len(kernel), 0,-1):  #kernel rows
                    for kerny in range(len(kernel[0]), 0, -1):     #kernel columns
                        #print("kernel", "kerny",kerny)
                        out = kernel[kernx-1][kerny-1] * arr[padx][pady]
                        #print("kernval", kernel[kernx-1][kerny-1])
                         
                        sum = sum + out
                
                #output array
                arrout.append(sum)
                
                #reset sum for next loop
                sum = 0   
    return arrout

#print("padded", padded)

#calcpixel(idkern5, padded)

#print("idkern", idkern5, "\n")

#print("padded array", padded)

if __name__ == '__main__':
    #variables
    kernel = onekern5
    array = cropped     # arr5
    num = 5
    
    #no change to these
    #padded = zero_pad(kernel, array)
    #arrout = calcpixel(kernel, padded)
    #print(np.array(arrout).reshape(num, num))
    
    
"""
#try numpy function: np.pad
print("numpy built in edge pad:")
builtin = np.pad(arr3, (1,1), 'edge')
print(builtin)
"""
#built in numpy functions


#next: crop an image to a square and pass it through the filter. compare to built-ins.

