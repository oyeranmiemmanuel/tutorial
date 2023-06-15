import docx

doc= docx.Document('result.doc')
print(len(doc.paragraphs))