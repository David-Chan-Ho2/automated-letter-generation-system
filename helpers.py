from docx import Document
import pandas as pd
import io

def extract_data_csv(pathfile):
    df = pd.read_csv(pathfile)
    return df.to_dict(orient='records')

def dict2tuples(data):
    return [tuple(v for k, v in d.items() if k != 'id') for d in data]

def append_doc(parent_doc, child_bytes):
    child_stream = io.BytesIO(child_bytes)
    child_doc = Document(child_stream)

    for element in child_doc.element.body:
        parent_doc.element.body.append(element)