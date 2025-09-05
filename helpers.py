import csv
from docx import Document

def extract_data_csv(pathfile):
    data = [] 
    
    with open(pathfile, "r") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append(row)
            
    return data

def append_docx(src_path, dest_path):
    dest_doc = Document(dest_path)
    src_doc = Document(src_path)

    for element in src_doc.element.body:
        dest_doc.element.body.append(element)

    dest_doc.save(dest_path)