from os import path
from os import replace
from os import listdir
from pathlib import Path

def move_imgs() -> None: 
    img_folder = path.abspath("output_imgs")
    root_dir = Path(__file__).parent.parent.parent
    for file in listdir(root_dir):
        if file.endswith(".png"):
            src_img_path = path.join(root_dir, file)
            dest_img_path = path.join(img_folder, file)
            replace(src_img_path, dest_img_path)
