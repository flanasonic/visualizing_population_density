#!/bin/bash

THIS_DIR=$(dirname -- $(readlink -f ${BASH_SOURCE}) )
if [ ! -d ${THIS_DIR}/venv ]
then
	echo "Creating Virtual Environment"
	python -m venv venv
	pip -r requirements.txt
fi

echo "Activating Virtual Environment..."

if [[ "$OSTYPE" =~ ^msys ]]; then
   ${THIS_DIR}/venv/Scripts/activate
   export PATH=${THIS_DIR}/venv/Scripts:$PATH    
else
   source ${VENV_SCRIPT}/venv/bin/activate
   export PATH=${THIS_DIR}/venv/bin:$PATH
fi
export VIRTUAL_ENV


echo "Staring Visual Studio Code"

code ./
