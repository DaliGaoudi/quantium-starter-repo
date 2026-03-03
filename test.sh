#!/bin/bash

# Stop script if any command fails
set -e

# Path to your virtual environment (adjust if needed)
VENV_DIR="venv"

# Activate virtual environment
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
else
    echo "Virtual environment not found!"
    exit 1
fi

# Run test suite (adjust command if you use something else)
pytest

# If pytest exits successfully, script exits with 0 automatically
exit 0