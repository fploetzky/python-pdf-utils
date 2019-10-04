from PyPDF2 import PdfFileWriter, PdfFileReader
from tabulate import tabulate
import shutil


class PdfMetadata:

    @staticmethod
    def get_tag(attribute):
        return '/' + attribute.capitalize()

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.file_handle = None
        self.pdfreader_handle = None
        self.metadata = None

        self.reload_file()

    def reload_file(self):
        if hasattr(self.file_handle, 'close'):
            self.file_handle.close()

        self.file_handle = open(self.pdf_path, 'rb')
        self.pdfreader_handle = PdfFileReader(self.file_handle)
        self.load_metadata()

    def load_metadata(self):
        self.metadata = self.pdfreader_handle.getDocumentInfo()

    def __str__(self):
        tab = tabulate(
            [(x[1:], self.metadata[x]) for x in self.metadata])
        return str(tab)

    def write_metadata_to_file(self, new_metadata):
        new_filename = self.pdf_path + '.pdf'
        writer = PdfFileWriter()

        for p in range(0, self.pdfreader_handle.numPages):
            writer.addPage(self.pdfreader_handle.getPage(p))

        writer.addMetadata(new_metadata)

        with open(new_filename, 'wb') as f:
            writer.write(f)

        self.file_handle.close()
        shutil.move(new_filename, self.pdf_path)
        self.reload_file()

    def write_metadata(self, title="", author="", subject="", keywords=""):
        new_metadata = {}
        if title != "":
            new_metadata[PdfMetadata.get_tag('title')] = title
        if author != "":
            new_metadata[PdfMetadata.get_tag('author')] = author
        if subject != "":
            new_metadata[PdfMetadata.get_tag('subject')] = subject
        if keywords != "":
            new_metadata[PdfMetadata.get_tag('keywords')] = keywords

        self.write_metadata_to_file(new_metadata)
