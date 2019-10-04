from PyPDF2 import PdfFileReader, PdfFileMerger


class PdfMerge:

    def __init__(self, files):
        self.files = files
        self.pdf_handles = None

        self._open_files()

    def _open_files(self):
        self.pdf_handles = [PdfFileReader(open(x, 'rb')) for x in self.files]

    def merge_pdf_files(self, output_file):
        merger = PdfFileMerger()
        for handle in self.pdf_handles:
            merger.append(handle)

        with open(output_file, 'wb') as f:
            merger.write(f)
