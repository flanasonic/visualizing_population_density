#!/bin/bash

THIS_DIR=$(dirname -- $(readlink -f ${BASH_SOURCE}) )
if [ ! -d ${THIS_DIR}/venv ]
then
	echo "Creating Virtual Environment..."
	python -m venv venv
fi

echo "Activating Virtual Environment..."

if [[ "$OSTYPE" =~ ^msys ]]; then
   source ${THIS_DIR}/venv/Scripts/activate
else
   source ${VENV_SCRIPT}/venv/bin/activate
fi

echo "Installing required packages..."
python -m pip install --disable-pip-version-check -q -r "${THIS_DIR}/requirements.txt"

echo "Staring Visual Studio Code..."

code ./

echo " "
echo "To run jupyter lab execute the following commands: "

if [[ "$OSTYPE" =~ ^msys ]]; then
   echo "  source ${THIS_DIR}/venv/Scripts/activate"
else
   echo "  source ${VENV_SCRIPT}/venv/bin/activate"
fi

echo "  jupyter lab"
