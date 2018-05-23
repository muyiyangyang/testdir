#!/usr/bin/python

def openfile(filepath):
    with open(filepath, 'r+') as f:
        data = f.read()
        print data

openfile('/root/testgit/test7.py')
