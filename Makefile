# Variables
PYTHON := python3
TEST_DIR := tests
DATA_SCRIPT := generate_test_data.py
MAIN_SCRIPT := main.py
DATA_FILE := ip_app_data.json

.PHONY: all data test

all: data test

# Target to generate test data
data:
	$(PYTHON) $(DATA_SCRIPT)

# Target to run unit tests
test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)
