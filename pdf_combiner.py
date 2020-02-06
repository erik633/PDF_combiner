import PyPDF2
import os
import re


def pdf_combiner(path):
    if os.path.exists(path):
        list_of_pdfs = []
        merger = PyPDF2.PdfFileMerger()
        for item in os.listdir(path):
            for match in re.finditer(r'\w+.pdf$', item):
                file = match.group(0)
                list_of_pdfs.append(file)
        print(list_of_pdfs)
        for pdf in list_of_pdfs:
            merger.append(pdf)
        merger.write("combinedPDF.pdf")
    else:
        print("Your directory path hasn't been found. Please, try it again...")


pdf_combiner("/Use/Folder/")