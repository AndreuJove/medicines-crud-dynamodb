#!/bin/bash

set -u
set -e

python3 -m venv lambda-venv

source lambda-venv/bin/activate

pip install -r requirements/requirements.txt

deactivate

cd lambda-venv/lib/python3.8/site-packages

zip -r ../../../../lambda-zip.zip .

cd ../../../../

zip -r lambda-zip.zip src

rm -rf lambda-venv
