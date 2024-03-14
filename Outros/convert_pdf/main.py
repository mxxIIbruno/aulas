"""
    Módulo PyMuPDF
    pip install PyMuPDF python-docx
"""
import fitz
from docx import Document


def pdf_to_word(pdf_path, word_path):
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    # Criar um documento Word
    doc = Document()

    # Iterar sobre as páginas do PDF
    for page_number in range(pdf_document.page_count):
        # page = pdf_document[page_number]

        # Extrair o texto da pádina
        # text = page.get_text("text")

        # doc.add_paragraph(text)
        ...

    # Salvar o ducumneto Word
    doc.save(word_path)

    # Fechar o arquivo PDF
    pdf_document.close()


# Exemplo de uso
pdf_file_path = "caminho\\do\\seu\\arquivo.pdf"
word_file_path = "caminho\\do\\seu\\arquivo.docx"

pdf_to_word(pdf_file_path, word_file_path)
