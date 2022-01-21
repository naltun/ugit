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

    return parser.parse_args()


def init(args):
    '''
    Frontend to initialize a `ugit' repository.
    '''
    data.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')
