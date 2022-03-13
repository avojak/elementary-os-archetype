#!/usr/bin/env python3

import cookiecutter.generate
import getpass
import os
import pwd
import re
import sys

from .archetype import Archetype
from datetime import datetime
from pathlib import Path

"""
"""
class ElementaryOsArchetype():

    _USER_APP_DIR = os.path.join(str(Path.home()), '.elementary-os-archetype')

    _DEFAULT_DEV_USERNAME = getpass.getuser()
    # https://stackoverflow.com/questions/15031137/full-unix-username-of-a-user#comment95623776_15031204
    _DEFAULT_DEV_FULLNAME = pwd.getpwuid(os.getuid())[4].split(',')[0]
    _DEFAULT_YEAR = str(datetime.now().year)
    _PROVIDED_TEMPLATE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
    _USER_TEMPLATE_ROOT = os.path.join(_USER_APP_DIR, 'templates')

    _REQUIRED_VARIABLES=['org_username', 'project_display_name', 'project_simple_name', 'project_namespace', 'project_id']
    _OPTIONAL_VARIABLES=['org_fullname', 'org_email', 'org_website', 'project_vcs']

    def __init__(self):
        # Create the application dir in the user home folder
        if not os.path.isdir(self._USER_APP_DIR):
            os.mkdir(self._USER_APP_DIR)
        # Create the user templates dir
        if not os.path.isdir(self._USER_TEMPLATE_ROOT):
            os.mkdir(self._USER_TEMPLATE_ROOT)
        return
    
    def _load_templates(self):
        archetypes=list()
        # Load provided templates
        for template_dir in [d for d in os.listdir(self._PROVIDED_TEMPLATE_ROOT) if os.path.isdir(os.path.join(self._PROVIDED_TEMPLATE_ROOT, d))]:
            archetypes.append(Archetype(os.path.join(self._PROVIDED_TEMPLATE_ROOT, template_dir)))
        # Load user-defined templates
        for template_dir in [d for d in os.listdir(self._USER_TEMPLATE_ROOT) if os.path.isdir(os.path.join(self._USER_TEMPLATE_ROOT, d))]:
            archetypes.append(Archetype(os.path.join(self._USER_TEMPLATE_ROOT, template_dir)))
        return archetypes
    
    def _load_template(self, name):
        for template in self._load_templates():
            if template.descriptor['name'] == name:
                return template
        # for template_dir in [d for d in os.listdir(self._PROVIDED_TEMPLATE_ROOT) if os.path.isdir(os.path.join(self._PROVIDED_TEMPLATE_ROOT, d)) and d == name]:
        #     return Archetype(os.path.join(self._PROVIDED_TEMPLATE_ROOT, template_dir))
        return None

    def list(self):
        templates = self._load_templates()
        print('Available templates:')
        for template in templates:
            print('  {}'.format(template.to_string()))

    def create(self, name):
        # Load the template
        template = self._load_template(name)
        if template is None:
            print('No template found for the name \"{}\"'.format(name))
            exit(-1)
        
        # Initialize the variable context
        context = dict()
        context['cookiecutter'] = dict()
        
        # Prompt for variables
        context['cookiecutter']['org_username'] = self._prompt_org_username()
        context['cookiecutter']['org_fullname'] = self._prompt_org_fullname()
        context['cookiecutter']['org_email'] = 'andrew.vojak@gmail.com' # TODO
        context['cookiecutter']['org_website'] = 'https://avojak.com' # TODO
        context['cookiecutter']['project_display_name'] = self._prompt_project_display_name()
        context['cookiecutter']['project_simple_name'] = self._prompt_project_simple_name(context['cookiecutter']['project_display_name'])
        context['cookiecutter']['project_namespace'] = self._prompt_project_namespace(context['cookiecutter']['project_display_name'])
        context['cookiecutter']['project_id'] = self._prompt_project_id(context['cookiecutter']['org_username'], context['cookiecutter']['project_simple_name'])
        
        # Other variables that won't be prompted
        context['cookiecutter']['year'] = self._DEFAULT_YEAR

        if 'extra_variables' in template.descriptor:
            for var in template.descriptor['extra_variables']:
                context['cookiecutter'][var] = input("{}: ".format(var))
        print(context)

        try:
            cookiecutter.generate.generate_files(template.path, context=context)
        except cookiecutter.exceptions.OutputDirExistsException as e:
            print("A directory with the name \"{}\" already exists!".format(context['cookiecutter']['project_simple_name']))
            sys.exit(-1)
    
    def _prompt_org_username(self):
        # TODO: Validate the input
        return input("Organization username (Default: {}): ".format(self._DEFAULT_DEV_USERNAME)).strip() or self._DEFAULT_DEV_USERNAME

    def _prompt_org_fullname(self):
        # TODO: Validate the input
        return input("Organization full name (Default: {}): ".format(self._DEFAULT_DEV_FULLNAME)).strip() or self._DEFAULT_DEV_FULLNAME
    
    def _prompt_project_display_name(self):
        res = ''
        while res == '':
            # TODO: Validate the input
            res = input("Project display name: ").strip()
        return res
    
    def _prompt_project_simple_name(self, project_display_name):
        # Convert spaces to '-' and make lowercase
        default_simple_name = project_display_name.replace(' ', '-').lower()
        # Remove any non-alphanumeric (or '-')
        default_simple_name = re.sub(r"[^a-zA-Z0-9/-]", "", default_simple_name)
        # TODO: Validate the input
        return input("Project simple name (Default: {}): ".format(default_simple_name)) or default_simple_name

    def _prompt_project_namespace(self, project_display_name):
        # Convert to title-case TODO: This should respect current capitalization too (e.g. WhaleWatcher)
        default_namespace = project_display_name.title()
        # Strip non-alphanumeric characters
        default_namespace = re.sub(r"[^a-zA-Z0-9]", "", default_namespace)
        # TODO: Validate the input
        return input("Project namespace (Default: {}): ".format(default_namespace)) or default_namespace
    
    def _prompt_project_id(self, org_username, project_simple_name):
        # TODO: Support non-GitHub IDs
        default_id = 'com.github.{org}.{app}'.format(org=org_username, app=project_simple_name)
        # TODO: Validate the input
        return input("Project ID (Default: {}): ".format(default_id)) or default_id