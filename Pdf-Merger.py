#   pip install pypdf2

import PyPDF2

print("Welcome to PDF Merger project Created by Indir Solanki")

files = ["1.pdf", "2.pdf", "3.pdf"]

merger = PyPDF2.PdfMerger()

for filename in files:
    files = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(files)
    merger.append(pdfReader)

files.close()
merger.write("merged.pdf")
