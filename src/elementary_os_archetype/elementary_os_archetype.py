#!/usr/bin/env python3

import cookiecutter.generate
import getpass
import os
import pwd

from .archetype import Archetype

"""
"""
class ElementaryOsArchetype():

    _DEFAULT_DEV_USERNAME = getpass.getuser()
    # https://stackoverflow.com/questions/15031137/full-unix-username-of-a-user#comment95623776_15031204
    _DEFAULT_DEV_FULLNAME = pwd.getpwuid(os.getuid())[4].split(',')[0]
    _ARCHETYPE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'archetypes'))

    def __init__(self):
        return
    
    def _load_archetypes(self):
        archetypes=list()
        for archetype_dir in [d for d in os.listdir(self._ARCHETYPE_ROOT) if os.path.isdir(os.path.join(self._ARCHETYPE_ROOT, d))]:
            archetypes.append(Archetype(os.path.join(self._ARCHETYPE_ROOT, archetype_dir)))
        return archetypes
    
    def _load_archetype(self, name):
        for archetype_dir in [d for d in os.listdir(self._ARCHETYPE_ROOT) if os.path.isdir(os.path.join(self._ARCHETYPE_ROOT, d)) and d == name]:
            return Archetype(os.path.join(self._ARCHETYPE_ROOT, archetype_dir))
        return None

    def list(self):
        archetypes = self._load_archetypes()
        print('Available archetypes:')
        for archetype in archetypes:
            print('  {}'.format(archetype.to_string()))

    def create(self, name):
        archetype = self._load_archetype(name)
        if archetype is None:
            print('No archetype found for the name \"{}\"'.format(name))
            exit(-1)
        context = dict()
        context['cookiecutter'] = dict()
        for var in archetype.descriptor['variables']:
            context['cookiecutter'][var] = input("{}: ".format(var))
        print(context)
        # context = dict()
        # context['cookiecutter'] = dict()
        # context['cookiecutter']['repo_name'] = 'monkeys'
        # cookiecutter.generate.generate_files(os.path.join(self._ARCHETYPE_ROOT, name), context=context)