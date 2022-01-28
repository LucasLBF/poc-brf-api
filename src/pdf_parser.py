from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re
from src.get_images import get_images
from src.utils import fetch_data as fd
from src.utils import move_imgs as mv


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
        results = []
        # print(f'===== {file["name"].upper()} =====')
        for section in content: 
            if keyword in str(section[1]):
                results.append(section)
                count += 1
                get_images("dataset/habitos_de_consumo_snacks.pdf", section[0] - 1)
        # print(f'{count} seções encontradas')
    return results
    mv.move_imgs()

#  [
#       nome_do_pdf: {
#        secoes: [{pag, trecho}] 
#        n_secoes: 2,
#        imgs: []
#       },
#       
# ]
#        