#!/usr/bin/env python3
"""
A script that shows the command line arguments received by the script.
"""

import sys

# Print the number of arguments: the length of sys.argv minus the script name
print("Number of arguments:", len(sys.argv) -  1)

# Print the script name
print("Script name:", sys.argv[0])

# Print the arguments (EXCLUDING the script name)
print("Arguments:", sys.argv[1:])

# Loop and print each argument: note the indentation: print is nested inside the loop (belongs to the loop)
for i, arg in enumerate(sys.argv):
    print(f"  {i}:\t{arg}")