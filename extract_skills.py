from pyresparser import ResumeParser
from docx import Document

def extract_skills_from_file(filed):
    try:
        doc = Document()
        with open(filed, 'r') as file:
            doc.add_paragraph(file.read())
        doc.save("text.docx")
        data = ResumeParser('text.docx').get_extracted_data()
        return data['skills']
    except:
        data = ResumeParser(filed).get_extracted_data()
        return data['skills']
