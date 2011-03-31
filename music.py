#!usr/bin/python

import os
import sys
import glob

directory = '/home/gardn227/MB/'
match = '*'

List = glob.glob(directory+match)

for item in List:
    if item[-3:] != 'mp3':
        #workingfile = item[:-3]
        WorkingFilename = str(item.split('.')[0] + '".mp3')
        originalFilename = str(item)
        command = 'ffmpeg -i "' + originalFilename + '" "' + WorkingFilename
        remove = 'rm "' + item + '"'
        os.system(command)
        os.system(remove)
