import PyPDF2

pdf= open('result.pdf', 'rb')
pdf1Reader= PyPDF2.PdfFileReader(pdf)
pdfWriter= PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
	pdfWriter.addPage(pdf1Reader.getPage(pageNum))


pdfWriter.encrypt('swordfish')
result= open('encrypt.pdf', 'wb')
pdfWriter.write(result)
result.close()

print("DONE!!!!!!")