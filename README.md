# MMBDTP Python Masterclass

[![Python application](https://github.com/telatin/python-workshop/actions/workflows/python-app.yml/badge.svg)](https://github.com/telatin/python-workshop/actions/workflows/python-app.yml)

![MMBDTP Python Masterclass](include/title.png)

This repository contains some simple Python notebooks and CLI scripts to introduce Python to biologists,
used for the *MMBDTP Masterclass* (May 2024).

* [Prerequisites](prerequisites.md)

## Environment

```
# Create an environment with the required libraries
conda create -n pystart -y "python>=3.6" biopython pyfastx pandas seaborn matplotlib ipykernel
conda activate pystart
```

## Hello World!

It's common to approach a programming language writing some code that will generate the "Hello, World!" text.
This code in Python looks like:

```python
print("Hello, World!")
```

This command:

* can be executed in an interactive shell (just type `python` and get the shell; Ctrl-D to exit)
* saved as a file (script), for example *hello.py*, and executed as `python hello.py`
* run in a [Python notebook](https://colab.research.google.com)

## Python Notebooks

Python notebooks, also known as [Jupyter notebooks](https://jupyter.org/), are interactive documents that allow users to write and execute Python code in a web browser. 

They combine code, text, and visualizations, making it easy to create and share data analysis workflows. 

Python notebooks are widely used in data science and research communities for exploratory data analysis, prototyping, and documentation. See: [using Jupyter Notebooks](https://docs.climb.ac.uk/notebook-servers/using-jupyter/) from the CLIMB-BIG-DATA documentation.

* [Notebooks](first-steps/README.md)

## CLI (Command Line Interface) Project

Since we all are [CLI Gurus](https://mmbdtp.github.io/modules/unix/week_1__programme/) (from Week1 of the MMBDTP training), we want to write a simple command line script to translate sequences.

It is a conversation starter, so to say, and it should be improved during the workshop, or at least tested to identify weaknesses and potential improvements.


* [Scripts](project/README.md)

## Resources

There is an immense amount of training resources for Python, so I will list some to cover different media and learning styles:

* [Youtube video: Python in 30 minutes](https://youtu.be/kqtD5dpn9C8?si=JzurDYRFLrKs7x3Q): video, covers the basics with clarity
* [Think in Python, 3rd edition](https://allendowney.github.io/ThinkPython/): online book