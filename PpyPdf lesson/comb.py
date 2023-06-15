import PyPDF2



pdf1= open('cpp_tutorial.pdf', 'rb')
pdf2= open('flask.pdf', 'rb')
pdf1Reader= PyPDF2.PdfFileReader(pdf1)
pdf2Reader= PyPDF2.PdfFileReader(pdf2)
pdfWriter= PyPDF2.PdfFileWriter()


for pageNum in range (pdf1Reader.numPages):
	pageObj= pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)


for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes2.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1.close()
pdf2.close()
print("DONE!!!!")