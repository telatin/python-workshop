#!/usr/bin/env python3
"""
A script that reads an input file (expected to be in FASTA format)
and print the number of "codons" in each sequence.
This requires parsing the SEQUENCE, we will try using pyfastx
Now we will use argparse to parse the command line arguments,
and encapsulate the code in a function
"""
import argparse
import sys
import pyfastx
 
def parse_fastx(filpath, min_codons=0):
    # Parse sequence by sequence using pyfastx
    fx = pyfastx.Fastx(filpath)
    for name, seq in fx:
        num_codons = len(seq) // 3
        if num_codons >= min_codons:
            print(f"{name}\n\t{num_codons} codons (OK)")
        else:
            print(f"{name}\n\t{num_codons} codons (below the minimum of {min_codons})")


if __name__ == "__main__":
    # Create the parser object
    parser = argparse.ArgumentParser(description="Count the number of codons in each sequence")
    # Add the input file argument
    parser.add_argument("input_file", help="Input FASTA file")
    # Let's add a "--min-codons" argument
    parser.add_argument("--min-codons", type=int, default=0, help="Minimum number of codons to print")
    # Parse the arguments
    args = parser.parse_args()
 
    # Call the main function
    parse_fastx(args.input_file, args.min_codons)

# NOTE how cleaner the code is now
