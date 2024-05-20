#!/usr/bin/env python3
"""
A script that reads an input file (expected to be in FASTA format)
and print the sequence names.
"""

import sys

# Check if an input file was provided with an if-elif block
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


# Read file line by line, opening it in read mode
input_fh = open(input_file, "r")

# Loop over each line in the file
for line in input_fh:
    # Remove leading/trailing whitespace
    line = line.strip()

    # If the line starts with ">", it's a sequence name
    if line.startswith(">"):
        # Remove the ">" character
        seq_name = line[1:]
        print(seq_name)


# NOW TRY TO CHANGE THIS
# 1. What happens if you do not use the slicing operation [1:] in the line seq_name = line[1:]?
# 2. What happens if you remove the line.strip() function call?