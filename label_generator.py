import csv
import docx
from docx import Document

names = []
with open('export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            names.append (row[1] + " " + row[2])

row = 0;
col = 0;
document = Document()
table = document.add_table (rows = 1, cols = 3)

for i in range (1,len(names),2):      
    row = table.add_row().cells
    name1 = names [i]
    name2 = names [i+1]
    row[0].text = name1 + "\nHouse of Commons \nOttawa, Ontario \nCanada \nK1A 0A6 " 
    row[2].text = name2 + "\nHouse of Commons \nOttawa, Ontario \nCanada \nK1A 0A6 " 

document.save('labels_template.docx')
