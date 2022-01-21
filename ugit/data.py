'''
data.py - Manages the data in `.ugit' directory. Here will be the code that actually touches files
on disk.
'''
import os


GIT_DIR = '.ugit'


def init():
    '''
    Helper function to create the `ugit' directory. This initializes a `ugit' repository.
    '''
    os.makedirs(GIT_DIR)
