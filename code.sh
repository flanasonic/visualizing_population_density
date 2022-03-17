#!/bin/bash

THIS_DIR=$(dirname -- $(readlink -f ${BASH_SOURCE}) )
if [ ! -d ${THIS_DIR}/venv ]
then
  echo "Creating Virtual Environment..."
  if [[ "$OSTYPE" =~ ^mysys ]]; then
         python -m venv venv
  else
	 python3 -m venv venv
  fi
fi

echo "Activating Virtual Environment..."

if [[ "$OSTYPE" =~ ^mysys ]]; then
   source ${THIS_DIR}/venv/Scripts/activate
else
   source ${THIS_DIR}/venv/bin/activate
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
   echo "  source ${THIS_DIR}/venv/bin/activate"
fi

echo "  jupyter lab"
