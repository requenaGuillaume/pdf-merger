from PyPDF2 import PdfWriter
import os
import shutil

class Merger():
    def __init__(self, folder) -> None:
        self.folder = folder        

    def merge_pdf(self) -> None:
        pdf_files = os.listdir(self.folder)

        merger = PdfWriter()

        for pdf in pdf_files:
            full_path = self.folder + "\\" + pdf
            print("Found : " + full_path + " to merge")
            merger.append(full_path)

        new_file_title = "merged-pdf.pdf"
        merger.write(new_file_title)
        merger.close()

        shutil.move(new_file_title, self.folder)   
