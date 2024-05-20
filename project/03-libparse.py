#!/usr/bin/env python3
"""
A script that reads an input file (expected to be in FASTA format)
and print the number of "codons" in each sequence.
This requires parsing the SEQUENCE, we will try using pyfastx
"""

import sys
import pyfastx

# Check if an input file was provided
if len(sys.argv) < 2:
    # the variable sys.argv is a list containing the command-line arguments
    # sys.argv[0] is the script name itself
    print(f"Usage: python {sys.argv[0]} INPUT_FILE")
    # Exit (with error status 1)
    sys.exit(1)
elif len(sys.argv) > 2:
    print("You provided more arguments than required: " + " ".join(sys.argv[2:]))
    print("Ignoring the extra arguments...")
    

input_file = sys.argv[1]

# Parse sequence by sequence using pyfastx
fx = pyfastx.Fastx(input_file)
for name, seq in fx:
    num_codons = len(seq) // 3
    print(f"{name}\n\t{num_codons} codons")

# NOTE how cleaner the code is now
