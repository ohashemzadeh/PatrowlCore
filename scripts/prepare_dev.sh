#!/bin/bash

# python manage.py spectacular --file openapi-schema.json

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
