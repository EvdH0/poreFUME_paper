#!/bin/bash
curdir=`pwd`
echo $curdir

git clone https://github.com/EvdH0/poreFUME
cd poreFUME
git checkout 0144d743dd5e3c99be92af9f4b5e81269f04930f #Update with V1.2
install.sh
source env.sh

#This will download the input files as used by poreFUME and calculateResistome.ipynb
cd $curdir
wget http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_data_v2.tar.gz
tar -zxvf poreFUME_paper_data_v2.tar.gz


#This will download the output results as used in the paper. So you dont have to run poreFUME and calculateResistome.ipunb yourself. You can directly go to analyzeResistome.ipynb and interact with the data.
cd $curdir
#mkdir output
#cd output
wget http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_OUTPUT_v2.tar.gz
tar -zxvf poreFUME_paper_OUTPUT_v2.tar.gz


cd $curdir
mkdir inputFiles
cd inputFiles

#Download the raw sequence files from ENA, this will take a bit!
wget ftp.sra.ebi.ac.uk/vol1/ERA678/ERA678638/oxfordnanopore_native/Lib_B_poreCamp.tar.gz
tar -zxvf Lib_B_poreCamp.tar.gz
wget ftp.sra.ebi.ac.uk/vol1/ERA702/ERA702458/oxfordnanopore_native/LibraryA.tar.gz
tar -zxvf LibraryA.tar.gz

echo 'Open up calculateResistome.ipynb and analyzeResistome.ipynb to start analysing'
