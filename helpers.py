from docx import Document
import pandas as pd

def extract_data_csv(pathfile):
    df = pd.read_csv(pathfile)
    return df.to_dict(orient='records')

def append_docx(src_path, dest_path):
    dest_doc = Document(dest_path)
    src_doc = Document(src_path)

    for element in src_doc.element.body:
        dest_doc.element.body.append(element)

    dest_doc.save(dest_path)