from docxtpl import DocxTemplate
from docx import Document
import io

from db.db import DB
from db import config
from helpers import extract_data_csv, append_doc
from data import data
    
def main():
    csv_file = "files/data.csv"
    docfile = "files/letter.docx"
    output_path = "files/output.docx"
    
    db = DB(config.DB_NAME)
    db.create_table()
    
    clients = extract_data_csv(csv_file) 
    db.seed(clients)
    
    parent_doc = Document()

    for client in clients:
        doc = DocxTemplate(docfile)
        data.update(client)
        doc.render(data)

        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)

        append_doc(parent_doc, file_stream.getvalue())

    parent_doc.save(output_path)

    db.close()
            
if __name__ == "__main__":
    main()