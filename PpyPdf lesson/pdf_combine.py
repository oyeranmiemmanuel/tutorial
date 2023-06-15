import PyPDF2

pdf1= open('cpp_tutorial.pdf', 'rb')
pdf2= open('flask.pdf', 'rb')
pdf1Reader= PyPDF2.PdfFileReader(pdf1)
pdf2Reader= PyPDF2.PdfFileReader(pdf2)
pdfWriter= PyPDF2.PdfFileWriter()
pdf_cmb = open('combinedminutes.pdf', 'rb')
cmb_reader= PyPDF2.PdfFileReader(pdf_cmb)
# page_1= pdf2Reader.getPage(2).extractText()
page_1= pdf2Reader.getPage(2)
cmb_1= cmb_reader.getPage(2)
# print(page_1.extractText())



# page_1.mergePage(cmb_1)
# pdfWriter.addPage(page_1)

result= open('result.doc', 'w')
result.write(page_1)
result.close()
print("DONE!!!!!")


result= open('result.pdf', 'wb')
pdfWriter.write(page_1)
result.close()
print("DONE!!!!!")



rotating the page
page=pdf1Reader.getPage(0)
page.rotateClockwise(90)



to merge page or overlay
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))




# for pageNum in range (pdf1Reader.numPages):
# 	pageObj= pdf1Reader.getPage(pageNum)
# 	pdfWriter.addPage(pageObj)


# for pageNum in range(pdf2Reader.numPages):
# 	pageObj = pdf2Reader.getPage(pageNum)
# 	pdfWriter.addPage(pageObj)

# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
pdf1.close()
pdf2.close()
print("DONE!!!!")