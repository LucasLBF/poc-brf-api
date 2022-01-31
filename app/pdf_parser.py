from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re
from app.utils import fetch_data as fd
from app.utils import move_imgs as mv
from app import get_images as img


def parse_pdfs(keyword: str) -> None:
    files = fd.fetch_data()

    results = []
    for file in files:
        pages = extract_pages(file["path"])
        content = []
        for page in pages:
            for elem in page:
                if isinstance(elem, LTTextContainer):
                    content.append((page.pageid, re.sub(r'[\n]', '', elem.get_text())))
        count = 0
        result = dict()
        result["nome"] = file["name"]
        result["secoes"] = []
        for section in content: 
            if keyword in str(section[1]):
                result["secoes"].append({ "pag": section[0], "trecho": section[1]}) 
                count += 1
                img.get_images(f"dataset/{file['name']}", section[0] - 1)
        result["n_secoes"] = count
        results.append(result)
    mv.move_imgs()
    return results

# V1
#  [
#       {
#        nome: blabla,
#        secoes: [{pag, trecho}] 
#        n_secoes: 2,
#        imgs: []
#       },
#       
# ]
#        
# V2
# [
#   {
#       type: "text" | "image",
#       source: string, 
#       page: int,
#       content: str | img_path,
#       highlight: str
#   } 
# ]