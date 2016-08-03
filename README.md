# poreFUME_paper
This repo allows to reproduce the analysis in the poreFUME paper.
Run ```run.sh``` to setup the analysis, this will:

1.  Clone into [poreFUME](https://github.com/EvdH0/poreFUME).
2.  Download the [input nanopore, PacBio and Sanger sequence data files](http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_data.tar.gz)
3.  Download the [processed data files by poreFUME](http://www.student.dtu.dk/~evand/poreFUME_data/poreFUME_paper_OUTPUT.tar.gz), these are not strictly necessary, but allow the user to skip the poreFUME pipeline itself
4.  Run ```install.sh``` of [poreFUME](https://github.com/EvdH0/poreFUME) which takes care of the [daligner](https://github.com/thegenemyers/DALIGNER), [DAZZ_DB](https://github.com/thegenemyers/DAZZ_DB), [POA](http://sourceforge.net/projects/poamsa/), [nanocorrect](https://github.com/jts/nanocorrect) dependencies.

Next you can check out the [calculateResistome.ipynb](calculateResistome.ipynb) notebook to run poreFUME and some auxiliary analysis (ie. sequence identity to the Sanger set) or directly go to [analyzeResistome.ipynb](analyzeResistome.ipynb) to reproduce the figures in the paper

## Dependencies
Minimal Python 2.7, pandas, numpy, biopython as described in the [poreFUME install](https://github.com/EvdH0/poreFUME/blob/master/INSTALL.md) document.  
poreFUME makes use of the [CARD database](https://card.mcmaster.ca/). So when using please cite [McArthur et al. 2013. The Comprehensive Antibiotic Resistance Database. Antimicrobial Agents and Chemotherapy, 57, 3348-3357](http://www.ncbi.nlm.nih.gov/pubmed/23650175). Furthermore [Nanocorrect](https://github.com/jts/nanocorrect) is used, which can be cited by [Loman NJ, Quick J, Simpson JT: A complete bacterial genome assembled de novo using only nanopore sequencing data. Nat Methods 2015, 12:733–735.](http://www.nature.com/nmeth/journal/v12/n8/abs/nmeth.3444.html)


## poreFUME
Check the [poreFUME README](https://github.com/EvdH0/poreFUME/README.md) and [poreFUME install](https://github.com/EvdH0/poreFUME/INSTALL.md) documents for more details and specific dependencies of poreFUME.
