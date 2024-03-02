from PyPDF2 import PdfWriter, PdfReader

class Splitter():
    def __init__(self) -> None:
        self.writer = PdfWriter()        

    # Public function
    def split(self, pack: bool) -> None:
        file_to_split = "pdf_files/to_split.pdf"

        with open(file_to_split, 'rb') as infile:
            reader = PdfReader(infile)
            self.page = 0
            total_pages = len(reader.pages)

            while self.page < total_pages :
                self.writer.add_page(reader.pages[self.page])

                if(pack):
                    self.split_pack(total_pages)
                else:
                    self.split_classic()

    # Private functions
    def split_classic(self) -> None:
        with open("pdf_files/output-{}.pdf".format(self.page), 'wb') as outfile:
            self.writer.write(outfile)

        self.page += 1

    def split_pack(self, total_pages) -> None:
        if(self.page == int(total_pages/3) or self.page == total_pages - 1):
            with open("pdf_files/output-{}.pdf".format(self.page), 'wb') as outfile:
                self.writer.write(outfile)

        self.page += 1
