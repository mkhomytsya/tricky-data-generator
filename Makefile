SHELL := /bin/bash
VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: help venv activate deactivate generate random-image copies clean clean-venv all

help:
	@echo "Available targets:"
	@echo "  venv          Create virtualenv and install requirements"
	@echo "  activate      Show how to activate the environment"
	@echo "  deactivate    Show how to deactivate the environment"
	@echo "  generate      Run both generators (random-image + copies)"
	@echo "  random-image  Generate one random image (uses generate_random_image.py)"
	@echo "  copies        Generate copies from a placeholder (uses generate_copies.py)"
	@echo "  clean         Remove generated output directory"
	@echo "  clean-venv    Remove the virtualenv (.venv)"
	@echo "  all           Create venv and run generators"

venv: $(VENV)/bin/activate

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@echo "Virtualenv ready in $(VENV). Activate with: source $(VENV)/bin/activate"

activate:
	@echo "Run: source $(VENV)/bin/activate"

deactivate:
	@echo "Run: deactivate  # after you have activated the venv in your shell"

generate: random-image copies

random-image:
	@# Prefer venv Python if available, fallback to system python3
	@if [ -x "$(PY)" ]; then $(PY) generate_random_image.py --outdir output; else python3 generate_random_image.py --outdir output; fi

copies:
	@# Uses a placeholder path; adjust as needed
	@if [ -x "$(PY)" ]; then $(PY) generate_copies.py --type image --placeholder placeholder.png --outdir output; else python3 generate_copies.py --type image --placeholder placeholder.png --outdir output; fi

clean:
	rm -rf output

clean-venv:
	rm -rf $(VENV)
	@echo "Removed $(VENV)"

all: venv generate
