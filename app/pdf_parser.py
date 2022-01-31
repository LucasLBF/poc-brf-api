from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re
from app.utils import fetch_data as fd
from app.utils import move_imgs as mv
from app import get_images as img


def parse_pdfs(keyword: str) -> None:
    files = fd.fetch_data()
    results = []
    count = 0
    for file in files:
        pages = extract_pages(file["path"])
        content = []
        for page in pages:
            for elem in page:
                if isinstance(elem, LTTextContainer):
                    content.append((page.pageid, re.sub(r'[\n]', '', elem.get_text())))
        for section in content: 
            if keyword in str(section[1]):
                count += 1
                result = {}
                result["type"] = "text"
                result["source"] = file["name"]
                result["highlight"] = keyword
                result["content"] = section[1]
                result["page"] = section[0]
                img.get_images(f"dataset/{file['name']}", section[0] - 1)
                results.append(result)
    imgs = mv.move_imgs(keyword)
    results += imgs
    return {"count": count, "results": results}


# V3
#  {
#   count: int,
#   results: [   
#       {
#           type: "text" | "image",
#           source: string, 
#           page: int,
#           content: str | img_path,
#           highlight: str
#       } 
#   ]
# }