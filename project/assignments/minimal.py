#!/usr/bin/env python3


#!/usr/bin/env python
"""
A script that reads an input file (expected to be in FASTA format)
and print the number of "codons" in each sequence.
This requires parsing the SEQUENCE, we will try using pyfastx
Now we will use argparse to parse the command line arguments,
and encapsulate the code in a function
"""
import argparse
import sys
import os
from Bio.Seq import Seq
import pyfastx
 
def parse_fastx(filePath, minCodons=0, geneticCodeId=1):
    # Parse sequence by sequence using pyfastx
    fx = pyfastx.Fastx(filePath)
    for name, seq in fx:
        num_codons = len(seq) // 3
        if num_codons >= minCodons:
            # See https://biopython.org/docs/1.75/api/Bio.Seq.html#Bio.Seq.Seq.translate
            aa = Seq(seq).translate(table=geneticCodeId)
            print(f">{name}\n{aa}")

if __name__ == "__main__":
    # Create the parser object
    parser = argparse.ArgumentParser(description="Count the number of codons in each sequence")
    # Add the input file argument
    parser.add_argument("input_file", help="Input FASTA file")
    # Let's add a "--min-codons" argument
    parser.add_argument("--min-codons", type=int, default=0, help="Minimum number of codons to print")
    parser.add_argument("--code", type=int, default=1, help="Genetic code to use")
    # Parse the arguments
    args = parser.parse_args()
 
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: file {args.input_file} not found")
        sys.exit(1)
    # Call the main function
    parse_fastx(args.input_file, args.min_codons, args.code)


 
