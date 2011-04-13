#!/usr/bin/python

import os
import sys
import glob

directory = raw_input('Directory? ')
directory = os.path.abspath(directory)
match = '/*'
Filelist = glob.glob(directory + match)

def ffmpeg(originalfile, newfile):
    '''
    this function allows us to run the unix tool ffmpeg with our music files.
    Takes two arguments, the first being the original filename and the second
    being the filename to which you would like to save the result.
    '''
    command = 'ffmpeg -y -i "' + originalfile + '" "' + newfile + '"'
    remove = 'rm "' + originalfile + '"'
    os.system(command)
    os.system(remove)



def FileHandling(folderlist):
    dirlist = []
    filelist = []
    for item in folderlist:
        if os.path.isdir(item):
            dirlist.append(item + '/')
        if os.path.isfile(item):
            filelist.append(item)
            
    for item in filelist:
        newitem = item.strip()
        newitemlist = item.split()
        newitem = ''.join(newitemlist)
        ffmpeg(item, newitem)
    for item in dirlist:
        FileHandling(item)


FileHandling(Filelist)
