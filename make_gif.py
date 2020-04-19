# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:29:39 2020

Author: Aalaap Nair

Description: Converts a series of .png images in a directory to a .gif
"""

import imageio as io
import os

#precise directory containing the images
target_directory=r"C:\Users\Aalaap Nair\Desktop\Projects\Freelunch Scripts\SKorea"

files=os.listdir(target_directory)
os.chdir(target_directory)

#files in directory sorrted by creation date
files.sort(key=os.path.getctime)


name=input("Name the output .gif:\n")
images=[]


for file in files:
    if file.endswith(".png"):
        file_path=os.path.join(target_directory,file)
        images.append(io.imread(file_path))


#duration between frames
io.mimsave(target_directory+"\\"+name+".gif", images, duration=0.5)