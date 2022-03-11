#!/usr/bin/env python3

import argparse
import sys

from .elementary_os_archetype import ElementaryOsArchetype
from .version import __version__

"""
"""
class CLI():

    def __init__(self):
        self.archetype = ElementaryOsArchetype()
        self.parser = argparse.ArgumentParser(prog='elementary-os-archetype')
        self.parser.set_defaults(func=lambda args: self.parser.print_help())
        self.parser.add_argument('-v', '--version', action='store_true', help='show the program version')
        subparsers = self.parser.add_subparsers(help='')

        parser_list = subparsers.add_parser('list', aliases=['l'], help='list available archetypes')
        parser_list.set_defaults(func=self._do_list)

        parser_create = subparsers.add_parser('create', aliases=['c'], help='create a new project from an archetype')
        parser_create.add_argument('name', type=str, help='the name of the archetype to use')
        # parser_create.add_argument('-f', '--file', type=str, help='a file containing variable definitions')
        parser_create.set_defaults(func=self._do_create)

    def run(self):
        args = self.parser.parse_args()
        if args.version:
            print('elementary OS Archetype {}'.format(__version__))
            sys.exit(0)
        args.func(args)

    def _do_list(self, args):
        self.archetype.list()
    
    def _do_create(self, args):
        self.archetype.create(args.name)

"""
The function that is called by the entrypoint script.
"""
def run():
    CLI().run()

"""
Allow the application to run via the module name as well (e.g. python3 -m elementary_os_archetype).
"""
if __name__ == "__main__":
    run()