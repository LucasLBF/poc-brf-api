from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re
from get_images import get_images
from utils import fetch_data as fd


def parse_pdfs(keyword: str) -> None:
    files = fd.fetch_data()

    for file in files:
        pages = extract_pages(file["path"])
        content = []
        for page in pages:
            for elem in page:
                if isinstance(elem, LTTextContainer):
                    content.append((page.pageid, re.sub(r'[\n]', '', elem.get_text())))
        count = 0
        print(f'===== {file["name"].upper()} =====')
        for section in content: 
            if keyword in str(section[1]):
                print(section)
                count += 1
                get_images("dataset/habitos_de_consumo_snacks.pdf", section[0] - 1)
        print(f'{count} seções encontradas')
