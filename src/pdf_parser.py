from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import os
import re
from pymupdf_ex import get_images

print("Digite uma palavra-chave: ")
keyword = input(">>> ")

pages = extract_pages(os.path.abspath("dataset/habitos_de_consumo_snacks.pdf"))
content = []

for page in pages:
    for elem in page:
        if isinstance(elem, LTTextContainer):
            content.append((page.pageid, re.sub(r'[\n]', '', elem.get_text())))

count = 0

for section in content: 
    if keyword in str(section[1]):
        print(section)
        count += 1
        get_images("dataset/habitos_de_consumo_snacks.pdf", section[0] - 1)
print(f'{count} seções encontradas')
