from docxtpl import DocxTemplate
import os

from db.db import DB
from db import config
from helpers import extract_data_csv, append_docx
from data import data
    
def main():
    csv_file = "files/data.csv"
    docfile = "files/letter.docx"
    output_path = "files/output.docx"
    
    db = DB(config.DB_NAME)
    db.create_table()
    
    clients = extract_data_csv(csv_file) 
    db.seed(clients)
        
    for i, client in enumerate(clients):
        doc = DocxTemplate(docfile)
        data.update(client)
        doc.render(data)
        input_file_path = f"input{i}.docx"
        doc.save(input_file_path)
        append_docx(input_file_path, output_path)

    for i, client in enumerate(clients):
        os.remove(f"input{i}.docx")
    
    db.close()
            
if __name__ == "__main__":
    main()
    
    