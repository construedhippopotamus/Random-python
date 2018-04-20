#-------------------------------------------------------------------------------
# Name:        tif2jpeg.py

# Author:      Jenny.Mital
#
# python 2.7

# Convert tif to jpeg for all tif in folder

# REQUIRES pillow (python image library)
# Pillow version 2.2.1


# to install pillow, go to C:\Python27\ArcGIS10.4\Scripts
# open cmd in that location
# type:  pip install Pillow==2.2.1
# it should install after that.

#this script will not overwrite files.

#-------------------------------------------------------------------------------
import os
from PIL import Image

#location of original tif files
path = r'M:\Mdata\163647\Library\As-builts\Caltrans Intranet\10'

# folder where the jpegs should be saved
savepath = r'M:\Mdata\163647\Library\As-builts\Caltrans Intranet\10\test\out'



#file counters
created = 0
exists = 0

os.chdir(path)

#list all files in folder
files = os.listdir(path)

for file in files:
    #process all .tif files
    if file.lower().endswith('tif'):

        im = Image.open(file)

        savefile = os.path.splitext(file)[0] + ".jpeg"
        #print(savefile)
        saveloc = os.path.join(savepath, savefile)
        #print("save location:", saveloc)
        if os.path.isfile(saveloc):
            exists += 1
        else:
            im.save(saveloc)
            print("Tiff created: ", saveloc)
            created +=1


    else:   #nothing happens for all non-tif extensions
        pass

print("%s jpegs created, %s already existing" %(created, exists))
