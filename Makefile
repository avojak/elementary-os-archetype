SHELL := /bin/bash

PACKAGE_NAME = elementary_os_archetype

SRC_DIR = src

.PHONY: all clean

all: venv-all

clean: venv-clean

include venv.mk