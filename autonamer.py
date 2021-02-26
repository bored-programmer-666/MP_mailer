import csv
import docx
from docx import Document

names = []
with open('export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            names.append (row[1] + " " + row[2])

for i in range (1,len(names)):
    document = Document('template.docx')
    for paragraph in document.paragraphs:
       if 'Name of Member of Parliament' in paragraph.text:
           mp_name = names [i]
           paragraph.text = paragraph.text.replace('Name of Member of Parliament', mp_name)
           document.save(mp_name + ".docx")

