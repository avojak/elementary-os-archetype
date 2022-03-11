#!/usr/bin/env python3

import os
import yaml

"""
"""
class Archetype():

    def __init__(self, dir):
        with open(os.path.join(dir, 'archetype.yaml'), 'r') as archetype_descriptor:
            try:
                self.descriptor = yaml.safe_load(archetype_descriptor)
            except yaml.YAMLError as error:
                print('Error while reading archetype descriptor {}:'.format(archetype_descriptor.name))
                print(error)
    
    def to_string(self):
        return '{name}: {description}'.format(name=self.descriptor['name'], description=self.descriptor['description'])