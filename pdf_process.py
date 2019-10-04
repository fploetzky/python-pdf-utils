#!/usr/bin/python3
import argparse

from pdftools.metadata import PdfMetadata
from pdftools.manipulation import PdfMerge


def parse_arguments():
    parser = argparse.ArgumentParser(description='Simple PDF Utility')
    parser.add_argument('--read_metadata',
                        '-r',
                        help='Provide the PDF file for metadata extraction')
    parser.add_argument('--edit_metadata',
                        '-e',
                        help='Provide a PDF file to edit a selection of metadata')
    parser.add_argument('--merge_pdfs',
                        '-m',
                        nargs='*',
                        help='PDF files to merge')
    parser.add_argument('--merge_output',
                        '-o',
                        default='mergeddef.pdf',
                        help='Name of the merged document')
    return parser.parse_args()


def read_metadata_from_file(file):
    reader = PdfMetadata(file)
    print(reader)


def read_metadata_from_cmd():
    return {
        'title':    input('Title: '),
        'author':   input('Author: '),
        'subject':  input('Subject: '),
        'keywords': input('Keywords: ')
    }


def edit_metadata(file):
    writer = PdfMetadata(file)
    writer.write_metadata(**(read_metadata_from_cmd()))


def merge_pdfs(pdfs, file_name='merged.pdf'):
    merge = PdfMerge(pdfs)
    merge.merge_pdf_files(file_name)


if __name__ == '__main__':
    arguments = parse_arguments()

    if arguments.read_metadata:
        read_metadata_from_file(arguments.read_metadata)

    if arguments.edit_metadata:
        edit_metadata(arguments.edit_metadata)

    if arguments.merge_pdfs:
        if arguments.merge_output != '':
            merge_pdfs(arguments.merge_pdfs, arguments.merge_output)
        else:
            print('Invalid file name for merged file')

