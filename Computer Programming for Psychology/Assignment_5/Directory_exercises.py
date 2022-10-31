# -*- coding: utf-8 -*-
"""
OS platform: WIN 11,i7
"""
import os,numpy
print(os.getcwd())

#Automate the creation of the list of images ("pics"). Do not write them all out manually.
pics = ["face"+str(f'{i:02}')+".jpg" for i in range(1,11) ]
print(pics)

#Automate the task of finding out whether each image (as listed in "pics") exists in the "images" directory.
#Use a for loop and if statements to print "cat1.jpg was found!", "cat2.jpg was found!"... etc. 
#Raise an exception if an image does not exist.
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
ims_in_dir = sorted(os.listdir(image_dir))

print(ims_in_dir)

for image in pics:
    if image in ims_in_dir:
        print(image+' was found!')
    else:
        raise Exception (image + ' not found!')

#Fill in the following sections of the experiment structure

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'data')
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')
#-check that these directories exist
#print(os.path.isdir(image_dir))
#print(os.path.isdir(data_dir))

if not os.path.isdir(image_dir):    
    raise Exception('Could not find the path-image!')

if not os.path.isdir(data_dir):
   raise Exception('Could not find the path-data!')

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist