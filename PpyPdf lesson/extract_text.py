import PyPDF2

pdf1= open('flask.pdf', 'rb')
pdf1Reader= PyPDF2.PdfFileReader(pdf1)
page2= pdf1Reader.getPage(15).extractText()


doc= open('docFile.doc', 'w')
doc.write(page2)
pdf1.close()
doc.close()



print("DONE!!!!!!")