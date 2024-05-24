#!/usr/bin/env python
"""
Created using ollama and model mixtral:8x22b and manual curation to fix errors and make it test.py compliant

SYSTEM REQUIREMENTS:
You are an expert Python and R developer with experience working with bioinformatics datasets such as genomes, metagenomes, and transcriptomes.
When using Python, you are keen on using Python, pandas and other well-known libraries.
You provide commented code to explain how to solve the problems.

USER:
make a python script to translate a FASTA file (DNA) to proteins. Use argparse to collect parameters (for example --code for the genetic table)

"""

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data import CodonTable
import pandas as pd

# Argument Parser for command line inputs
parser = argparse.ArgumentParser(description="Translate DNA sequences from a FASTA file to Proteins.")
parser.add_argument("FASTA",  help="The path of the input FASTA file")
parser.add_argument("--code", default=1, type=int, help="Genetic code table number (default: %(default)s). See Biopython docs for more information.")
parser.add_argument("--min-length", default=0, type=int, help="Minimum length of the protein sequence to be included in the output (default: %(default)s).")
args = parser.parse_args()

if args.FASTA.endswith(".gz"):
    import gzip
    with gzip.open(args.FASTA, "rt") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
else:
    # Load FASTA file and select the desired genetic code table
    records = list(SeqIO.parse(args.FASTA, "fasta"))
table = CodonTable.unambiguous_dna_by_id[args.code]

# Create a function to translate DNA sequences to protein sequences using the selected genetic code table
def dna_to_protein(record, table):
    return str(Seq(record.seq).translate(table=table))

# Apply the translation function and collect results in a pandas DataFrame
translated_sequences = pd.DataFrame({
    "ID": [rec.id for rec in records], 
    "Seq": [dna_to_protein(rec, table) for rec in records]
})

# Remove short ORFs
translated_sequences = translated_sequences[translated_sequences["Seq"].str.len() >= args.min_length]
# Print dataframe to fasta format
fasta_output = ""
for index, row in translated_sequences.iterrows():
    fasta_output += f">{row['ID']}\n{row['Seq']}\n"
print(fasta_output, end="")
