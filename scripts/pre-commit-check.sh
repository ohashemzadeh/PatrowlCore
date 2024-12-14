#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

VENV_DIRECTORY=venv

echo "Running autoflake..."
autoflake -i -r --ignore-init-module-imports --remove-all-unused-imports --exclude $VENV_DIRECTORY .
echo "${GREEN}Done${NC}"
printf "\n"

echo "Running autopep8..."
autopep8 --global-config pyproject.toml .
echo "${GREEN}Done${NC}"
printf "\n"


# Check if flake8 is installed
if flake8 --version >/dev/null 2>&1; then
    :  # Do nothing, similar to 'pass' in Python
else
    echo "flake8 is not installed. Installing..."
    pip3 install flake8
fi


echo "Running flake8..."
flake8 --config .flake8
echo "${GREEN}Done${NC}"
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