#!/usr/bin/env python3
"""
A script that reads an input file (expected to be in FASTA format)
and print the number of "codons" in each sequence.
This requires parsing the SEQUENCE, we will try without using libraries
"""

import sys

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


# Read file line by line, opening it in read mode
input_fh = open(input_file, "r")

# Temporary variables to store the current sequence name and sequence
current_seq_name = None
sequence = ""

# Loop over each line in the file
for line in input_fh:
    # Remove leading/trailing whitespace
    line = line.strip()

    
    
    # If the line starts with ">", it's a sequence name
    if line.startswith(">"):

        # Check if we have a previous sequence
        if current_seq_name is not None:
            # Count the number of codons in the sequence
            num_codons = len(sequence) // 3
            print(f"\t {num_codons} codons")
            # Reset the sequence
            sequence = ""
        else:
            print("No sequence found")

        # Remove the ">" character
        current_seq_name = line[1:]
        print(current_seq_name)
    else:
        sequence += line


# Check if we have a previous sequence after the loop ends
# WHY? 
if current_seq_name is not None:
    # Count the number of codons in the sequence
    num_codons = len(sequence) // 3
    print(f"\t {num_codons} codons")
    # Reset the sequence
    sequence = ""