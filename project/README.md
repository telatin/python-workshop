# A CLI project

Here we try to make a script for general use. 

### Goal 

Our goal is to write a simple script that reads an input file (expected to be in FASTA format) and prints the number of "codons" in each sequence.

### Arguments
 When making a CLI script the first part will be to define how the user will give us the parameters.

There is a standard library called argparse that will be fine for 90% of the projects, but first let's try to see how the arguments are passed to Python:

* [getting arguments (manually)](00-args.py)


### Reading an input file

We will need to read an input file in FASTA format. To learn Python it's OK to try to parse the content manually, but in real life we **must** use existing libraries...

* [reading a file](01-read.py)
* [manually parsing fasta](02-parse.py)

### Parsing a FASTA file

Now that we tried to manually read a FASTA file, we can use a library for the task.
Biopython will perfectly work and you should consider checking Biopython first as it is a comprehensive library (we will use it later), but to show how to use specific libraries we adopted *[pyfastx](https://pyfastx.readthedocs.io/en/latest/)* (faster).

* [parsing FASTA](03-libparse.py)

### Getting arguments from the CLI

Now we will add [argparse](https://docs.python.org/3/library/argparse.html) to parse parameters. This is a standard module, so we won't need to install it.

* [parsing FASTA and getting parameters](04-cliparse.py)

### Translating

Finally we are going to translate the sequences with [biopython](https://biopython.org):

* [translate program](05-translate.py)

