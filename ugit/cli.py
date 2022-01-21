'''
cli.py - In charge of parsing and processing user input.
'''
import argparse
import os

from . import data


def main():
    '''
    Entrypoint to `ugit'.
    '''
    args = parse_args()
    args.func(args)


def parse_args():
    '''
    Parse user-supplied arguments to `ugit'.
    '''
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    return parser.parse_args()


def init(args):
    '''
    Frontend to initialize a `ugit' repository.
    '''
    data.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')


def hash_object(args):
    '''
    Frontend to create a content-addressable storage of a file.
    '''
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))
