import PyPDF2

pdfFile = open('FILENAME', 'rb')                        # Input file name
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(First Page, Last Page + 1):        # Input page range, make sure to take any preambles and cover pages into consideration
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('NEWFILE.pdf', 'wb')               # This writes pages to a new doc 
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()