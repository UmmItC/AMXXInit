# SPDX-License-Identifier: MIT
VERSION = 0
PATCHLEVEL = 1
SUBLEVEL = 0
EXTRAVERSION = 
NAME = AMXXInit

help:
	@echo "Available targets:"
	@echo "  install   Install dependencies using pip"
	@echo "  run       Run the main.py script"
	@echo "  clean     Clean up temporary files"
	@echo "  check     Check if required files exist or not"

install:
	@echo "Installing dependencies..."
	pip3 install -r requirements.txt

run:
	@echo "Running AMXXInit..."
	python3 main.py

clean:
	@echo "Clean up Directory ..."
	rm -rfv metamod* amxmodx*

check:
	@if ! ls metamod* >/dev/null 2>&1 || ! ls amxxmod* >/dev/null 2>&1; then \
		echo "File not existing: metamod* or amxxmod*"; \
	else \
		echo "File exist!"; \
	fi
