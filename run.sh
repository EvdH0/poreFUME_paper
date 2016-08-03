#!/bin/bash
curdir=`pwd`
echo $curdir

git clone https://github.com/EvdH0/poreFUME
cd poreFUME
install.sh
source env.sh

#This will download the input files as used by poreFUME and calculateResistome.ipynb
cd $curdir
mkdir inputFiles
cd inputFiles
wget http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_data.tar.gz
tar -zxvf poreFUME_paper_data.tar.gz

#This will download the output results as used in the paper. So you dont have to run poreFUME and calculateResistome.ipunb yourself. You can directly go to analyzeResistome.ipynb and interact with the data.
cd $curdir
mkdir output
cd output
wget http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_OUTPUT.tar.gz
tar -zxvf poreFUME_paper_OUTPUT.tar.gz

echo 'Open up calculateResistome.ipynb and analyzeResistome.ipynb to start analysing'
