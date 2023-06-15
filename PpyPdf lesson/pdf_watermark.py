import PyPDF2

pdf1= open('cpp_tutorial.pdf', 'rb')
pdf2= open('flask.pdf', 'rb')

pdf1Reader= PyPDF2.PdfFileReader(pdf1)
pdf2Reader= PyPDF2.PdfFileReader(pdf2)
pdfWriter= PyPDF2.PdfFileWriter()


page_1= pdf2Reader.getPage(20)
page_2= pdf2Reader.getPage(10)


page_1.mergePage(page_2)
pdfWriter.addPage(page_1)

result= open('watermark.pdf', 'wb')
pdfWriter.write(result)
pdf1.close()
pdf2.close()
result.close()

print("DONE!!!!!!")

