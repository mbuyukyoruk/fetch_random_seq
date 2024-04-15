import random
import argparse
import sys
import subprocess
import re
import textwrap
import os

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python fetch_random_seq.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

# fetch_random_seq

Author: Murat Buyukyoruk

        fetch_random_seq help:

This script is developed to fetch random sequences from a multifasta to create less sequences (i.e. to generate subfasta for HMM file generation). 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python fetch_random_seq.py -i demo.fasta -n 5

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

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a alinged fasta file.\n')
parser.add_argument('-n', '--number', required=True, type=int, dest='random_number',
                    help='Specify a alinged fasta file.\n')

results = parser.parse_args()
filename = results.filename
random_number = results.random_number

acc_list = []
seq_list = []
desc_list = []

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

if random_number > length:
    print("Available number of sequences in fasta file is less that requested random sequences. Please enter number less than " + str(length))
    sys.exit()

else:
    pass

out = filename.split('.fasta')[0].split('/')[-1] + '_random_' + str(random_number) + '.fasta'

with tqdm.tqdm(range(length), desc='Reading fasta...') as pbar:
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        acc_list.append(record.id)
        desc_list.append(record.description)
        seq_list.append(record.seq)

num = len(acc_list)

select_list = (random.sample(acc_list, random_number))

os.system('> ' + out)

with tqdm.tqdm(range(len(select_list)), desc='Fetching...') as pbar:
    f = open(out, 'a')
    sys.stdout = f
    for i in range(len(select_list)):
        pbar.update()
        ind = acc_list.index(select_list[i])
        print(">" + desc_list[ind])
        print(re.sub("(.{60})", "\\1\n", str(seq_list[ind]), 0, re.DOTALL))