#!/bin/bash
THIS_DIR=$(dirname -- $(readlink -f ${BASH_SOURCE}) )

if [ ! -d data ]
then
        echo "Data folder does not exist... creating"
	mkdir -p ${THIS_DIR}/data
else
        echo "Data folder exists..."
fi

for f in  ${THIS_DIR}/data_archive/*.tgz
do
  cp ${f} ${THIS_DIR}/data
done

cd "${THIS_DIR}/data"

for f in *.tgz
do
   echo "unpacking ${f}"
   tar -xzvf ${f}
   rm "${f}"
done

echo " --- Done --- "

