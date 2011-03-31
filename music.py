#!usr/bin/python

import os
import sys
import glob

directory = '/home/gardn227/MB2/'
match = '*'
Filelist = glob.glob(directory+match)

def ffmpeg(originalfile, newfile):
    '''
    this function allows us to run the unix tool ffmpeg with our music files.
    Takes two arguments, the first being the original filename and the second
    being the filename to which you would like to save the result.
    '''
    command = 'ffmpeg -i "' + originalfile + '" "' + newfile + '"'
    remove = 'rm "' + originalfile + '"'
    os.system(command)
    os.system(remove)

def FindFiles(MainDir):
    '''
    Recursively descends into directories until it finds a file that is not
    a directory. Executes the requisite action, then backs out one directory
    and moves into the next sub-directory
    '''
    for item in Filelist:
        if os.path.isdir(item):
            FindFiles(item)
        else:
            (Name, Extension) = os.path.splittext(item)
            if Extension != '.mp3':
                NewName = Name.strip() + '.mp3'
                ffmpeg(item, NewName)
                
            
                



'''
for item in List:
    if item[-3:] != 'mp3':
        #workingfile = item[:-3]
        WorkingFilename = str(item.split('.')[0] + '".mp3')
        originalFilename = str(item)
        command = 'ffmpeg -i "' + originalFilename + '" "' + WorkingFilename
        remove = 'rm "' + item + '"'
        os.system(command)
        os.system(remove)
'''
