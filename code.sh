THIS_DIR=$(dirname -- $(readlink -f ${BASH_SOURCE}) )
if [ ! -d ${THIS_DIR}/venv ]
then
	echo "creating virtual environment"
	python -m venv venv
	pip -r requirements.txt
fi

VEN

if [[ "$OSTYPE" =~ ^msys ]]; then
   ${THIS_DIR}/venv/Scripts/activate
    
else
   source ${VENV_SCRIPT}/venv/bin/activate
fi

code ./
