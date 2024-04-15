# fetch_random_seq

Author: Murat Buyukyoruk

        fetch_random_seq help:

This script is developed to fetch random sequences from a multifasta to create less sequences (i.e. to generate subfasta for HMM file generation). 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain 
long and many sequences.

Syntax:

        python fetch_random_seq.py -i demo.fasta

fasta_unalignr dependencies:

Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download

tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a multi sequence alignment fasta file.

	-n/--number		Number			Specify number of sequences to be fetched randomly.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

