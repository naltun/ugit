'''
data.py - Manages the data in `.ugit' directory. Here will be the code that actually touches files
on disk.
'''
import hashlib
import os


GIT_DIR = '.ugit'


def init() -> None:
    '''
    Helper function to create the `ugit' directory. This initializes a `ugit' repository.
    '''
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data) -> str:
    '''
    Helper function to create content-addressable storage for our files.
    '''
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as f:
        f.write(data)
    return oid


def get_object(oid) -> bytes:
    '''
    Print the contents of a file, given the object ID.
    '''
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read()
