#!/bin/bash

# -u "unbound variable"
set -eu

echo "Installing python packages..."
pip3 install pre-commit==2.18.1


echo "Installing pre-commit hooks.."
pre-commit install
