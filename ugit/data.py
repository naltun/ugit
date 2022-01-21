'''
data.py - Manages the data in `.ugit' directory. Here will be the code that actually touches files
on disk.
'''
import hashlib
import os


GIT_DIR = '.ugit'


def init():
    '''
    Helper function to create the `ugit' directory. This initializes a `ugit' repository.
    '''
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data):
    '''
    Helper function to create content-addressable storage for our files.
    '''
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as f:
        f.write(data)
    return oid
