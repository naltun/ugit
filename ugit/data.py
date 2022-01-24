'''
data.py - Manages the data in `.ugit' directory. Here will be the code that actually touches files
on disk.
'''
import hashlib
import os


GIT_DIR = '.ugit'
NULL_BYTE = b'\x00'


class ObjectTypeError(Exception):
    pass


def init() -> None:
    '''
    Helper function to create the `ugit' directory. This initializes a `ugit' repository.
    '''
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data, obj_type='blob') -> str:
    '''
    Helper function to create content-addressable storage for our files.

    `obj' has an object header, which is the object's type, followed by a null byte. Proceeding this
    header is the object's content.

    Example object:
                    Object Header
                      |      |
                      |      |Object Content
                      |      ||           |
                      |______||___________|
                      v      vv           v
                    b'blob\x00Hello, World!'
    '''
    obj = obj_type.encode() + NULL_BYTE + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as f:
        f.write(obj)
    return oid


def get_object(oid, expected='blob') -> bytes:
    '''
    Print the contents of a file, given the object ID.
    '''
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read()

    obj_type, _, content = obj.partition(NULL_BYTE)
    obj_type = obj_type.decode()

    if expected and obj_type != expected:
        raise ObjectTypeError(f'Expected {expected}, got {obj_type}')
    return content
