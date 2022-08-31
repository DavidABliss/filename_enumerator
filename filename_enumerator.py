# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import argparse
import datetime

parser = argparse.ArgumentParser(description='Number (or renumber) all files in a directory, proceeding alphabetically. Attempt to use the existing filename template or provide a new template with -t')
parser.add_argument('inputPath', nargs='?', help='path to the files to be renamed', default=os.getcwd())
parser.add_argument('-t', '--template', action='store', dest='t', required=False, help='a custom template to be used as the basis for all new filenames in the directory')
parser.add_argument('-i', '--index', nargs='?', default=1, action='store', dest='i', type=int, help='the starting index number, from which all filename numbers will count up')
parser.add_argument('-d', '--digits', required=False, action='store', dest='d', type=int, help='the number of digits that will be used for file enumeration. default is the minimum number of digits required to enumerate all files')
parser.add_argument('-v', '--reverse', required=False, action='store_true', dest='v', help='reverse the enumeration, so the alphabetically-last file in the directory become the lowest-numbered')

args=parser.parse_args()

dirPath = os.path.abspath(args.inputPath)
os.chdir(dirPath)
fileNum = args.i
os.mkdir(os.path.join(dirPath,'renamed'))


def listCompiler(inputPath):
    fileList = []
    
    for item in os.listdir(dirPath):
        if os.path.isfile(item):
            fileList.append(item)
    if args.v:
        fileList.reverse()
    if not args.d:
        global digits
        digits = setDigits(fileList)
    elif args.d:
        digits = args.d
    for file in fileList:
        nameSplitter(file)

def setDigits(fileList):
    listCount = len(fileList)
    digits = len(str(listCount))
    return(digits)

def nameSplitter(file):
    root, extension = os.path.splitext(file)
    if not args.t:
        newRoot = numScrubber(root)
    elif args.t:
        newRoot = args.t
    renamer(file, newRoot, extension)
    
def numScrubber(root):
    newRoot = '_'.join(root.split('_')[:-1]) + '_'
    return(newRoot)

def renamer(file, newRoot, extension):
    global fileNum
    strNum = str(fileNum)
    num = strNum.zfill(digits)
    newName = newRoot + num + extension
    reportLine = file + ' -> ' + newName
    reportWriter(reportLine)
    fileNum += 1
    os.rename(file, os.path.join('renamed',newName))
    
def reportWriter(line):
    time = datetime.datetime.now()
    stringTime = time.strftime("%Y%m%d%H%M%S")
    with open(os.path.join(dirPath, 'rename' + stringTime + '.txt'), 'a', encoding='utf-8') as report:
        report.write(line + '\n')

listCompiler(dirPath)