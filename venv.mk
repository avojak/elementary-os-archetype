BUILD_DIR    = build
DIST_DIR     = dist
VENV_DIR     = env
VENV_BIN_DIR = $(VENV_DIR)/bin
PACKAGE_DIR  = $(SRC_DIR)/$(PACKAGE_NAME)

VERSION_FILE      = $(PACKAGE_DIR)/version.py
VERSION           = $(shell cat $(VERSION_FILE) | cut -d '=' -f2 | tr -d '"' | xargs)
REQUIREMENTS_FILE = requirements.txt

SYSTEM_PYTHON_EXECUTABLE = python3
PYTHON_EXECUTABLE        = $(VENV_BIN_DIR)/python3
PIP_EXECUTABLE           = $(VENV_BIN_DIR)/pip3.8

.PHONY: venv-all venv-init venv-requirements venv-clean

venv-all: venv-init venv-requirements venv-build

venv-init: $(PYTHON_EXECUTABLE) $(PIP_EXECUTABLE)

$(PYTHON_EXECUTABLE) $(PIP_EXECUTABLE):
	$(SYSTEM_PYTHON_EXECUTABLE) -m venv $(VENV_DIR)

venv-requirements:
	$(PIP_EXECUTABLE) install build
	$(PIP_EXECUTABLE) install -r $(REQUIREMENTS_FILE)

venv-build: # $(DIST_DIR)/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl
	$(PYTHON_EXECUTABLE) -m build --wheel

# $(DIST_DIR)/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl:
# 	$(PYTHON_EXECUTABLE) -m build --wheel

venv-clean:
	rm -rf $(VENV_DIR)
	rm -rf $(BUILD_DIR)
	rm -rf $(DIST_DIR)
	rm -rf $(SRC_DIR)/$(PACKAGE_NAME)/__pycache__
	rm -rf $(SRC_DIR)/$(PACKAGE_NAME).egg-info