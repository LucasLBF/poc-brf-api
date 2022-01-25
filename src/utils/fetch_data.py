from os import path
from os import listdir

# returns list of dictionaries
# [{ name: str, path: str }] 
def fetch_data() -> list:
    dataset_path = path.abspath("dataset")
    files = listdir(dataset_path)
    file_list = []
    for f in files:
        file_dict = dict()
        file_dict["name"] = f
        file_dict["path"] = path.join(dataset_path, f)
        file_list.append(file_dict)
    return file_list
        