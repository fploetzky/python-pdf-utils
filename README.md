# Python PDF Utilities
A collection of command line utilities for various operations on PDF files.

## What is this and why does it even exist?
During my university time PDF files have been omnipresent especially when it comes to lecture notes.
Aaaand normally the slide deck is divided into 12 or more parts or more which makes it uncomfortable
to read and especially to use in ebook readers. 

Another problem is the lack of metadata in most PDF files so the library of my Kobo ebook reader
usually contains a lot of books titled <random_guid><last_name_of_the_third_author>.pdf ...

On Windows various PDF tools (e.g. [PDF 24](https://tools.pdf24.org/de/creator) or 
[BeCyPDFMetaEdit (not the official homepage)](https://www.heise.de/download/product/becypdfmetaedit-36720))
are available but I have not found a simple tool for Debian Linux (okay I googled about 30 seconds but ... you get the point)
so this tools were designed for my personal use.

Maybe somebody out there is interested and find some use case. Or maybe not, this is mostly a small hobby project.

## Features
Some (planned) features:

*  merge PDF files into a single file
*  show PDF metadata on the command line
*  edit the PDF metadata (title, author, comment, sub title)

## Installation
For Debian and Ubuntu derivates:

1. Install python3 and python3-pip (apt install python3 python3-pip)
2. Install the requirements (pip install requirements/pip_requirements.req)
3. Set the executable bit for pdf_process.py (chmod +x pdf_process.py)

## Examples

Show the internal help:

``> pdf_process.py -h ``

Show the metadata of test.pdf

``> pdf_process.py -r test.pdf ``

Edit the metadata of test.pdf (the script will ask for title, author, subject and keywords):

``> pdf_process.py -e test.pdf``

Merge t1.pdf and t2.pdf into merged.pdf

``> pdf_process.py -m t1.pdf t2.pdf -o merged.pdf``

Merge all PDF files in the current folder into merged.pdf (the order is determined by the name of the files 
in lexicographical order):

``> pdf_process.py -m * -o merged.pdf``