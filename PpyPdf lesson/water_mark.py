import PyPDF2

pdf1= open('cpp_tutorial.pdf', 'rb')
pdf2= open('flask.pdf', 'rb')
pdf1Reader= PyPDF2.PdfFileReader(pdf1)
pdf2Reader= PyPDF2.PdfFileReader(pdf2)
pdfWriter= PyPDF2.PdfFileWriter()


page_1= pdf2Reader.getPage(2)
page_2= pdf1Reader.getPage(2)
page_1.mergePage(page_1)
pdfWriter.addPage(page_1)

pdfWatermarkReader = open('watermark1.pdf', 'wb')
pdfWriter.write(pdfWatermarkReader)
pdf1.close()
pdf2.close()
pdfWatermarkReader.close 