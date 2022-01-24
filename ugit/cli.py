'''
cli.py - In charge of parsing and processing user input.
'''
import argparse
import os
import sys

from . import data


def main() -> None:
    '''
    Entrypoint to `ugit'.
    '''
    args = parse_args()
    args.func(args)


def parse_args() -> argparse.Namespace:
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

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()


def init(args) -> None:
    '''
    Frontend to initialize a `ugit' repository.
    '''
    data.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')


def hash_object(args) -> None:
    '''
    Frontend to create a content-addressable storage of a file.
    '''
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))


def cat_file(args) -> None:
    '''
    Frontened to print the contents of a stored file.
    '''
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))
