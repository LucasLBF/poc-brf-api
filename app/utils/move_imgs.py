from os import path
from os import replace
from os import listdir
import re
from pathlib import Path

def move_imgs(highlight: str) -> list: 
    img_folder = path.abspath("output_imgs")
    root_dir = Path(__file__).parent.parent.parent
    imgs = []
    for file in listdir(root_dir):
        if file.endswith(".png"):
            page = re.search('p(\d*)-.*', file).group(1)
            source = re.search('.*-(.*).png', file).group(1)
            img = {}
            img["type"] = "image"
            img["source"] = source
            img["page"] = int(page) + 1
            img["filename"] = file
            img["highlight"] = highlight 
            imgs.append(img)
            src_img_path = path.join(root_dir, file)
            dest_img_path = path.join(img_folder, file)
            replace(src_img_path, dest_img_path)
    return imgs
            
