#!/bin/bash

set -e

DIRECTORY=.


GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color


echo "Running autoflake..."
autoflake -i -r --ignore-init-module-imports --remove-all-unused-imports --exclude venv $DIRECTORY
echo "${GREEN}Done${NC}"
printf "\n"

echo "Running autopep8..."
autopep8 --global-config pyproject.toml $DIRECTORY
echo "${GREEN}Done${NC}"
printf "\n"


echo "Running flake8..."
flake8 --config .flake8
echo "${GREEN}Done${NC}"
printf "\n"


echo "Running mypy..."
mypy --show-error-codes $DIRECTORY
printf "\n"


echo "Running pylint..."
pylint --rcfile=.pylintrc -j "$(nproc)" $DIRECTORY
printf "\n"


echo "Running tests..."
python3 PatrowlCore/manage.py test api

# Check if tests passed
if [ $? -eq 0 ]; then
    echo -e "${GREEN}TESTS PASSED${NC}"
else
    echo -e "${RED}TESTS FAILED${NC}"
fi

printf "\n"