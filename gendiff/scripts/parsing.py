"""Modul for parsing input filesge."""
import os
import json
import pathlib
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


# def generate_diff(filepath1, filepath2):
#     """Generate difference files."""
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     file_path_1 = pathlib.Path(dir_path, filepath1)
#     file_path_2 = pathlib.Path(dir_path, filepath2)
#     file_1 = json.load(open(file_path_1))   # dict
#     file_1 = dict(sorted(file_1.items()))
#     file_2 = json.load(open(file_path_2))
#     file_2 = dict(sorted(file_2.items()))
#     file_3 = {}

#     for key1 in file_1.keys():
#         if key1 in file_2.keys():
#             if file_1[key1] == file_2[key1]:
#                 file_3[f"  {key1}"] = file_1[key1]
#             else:
#                 file_3[f"- {key1}"] = file_1[key1]
#                 file_3[f"+ {key1}"] = file_2[key1]
#         else:
#             file_3[f'- {key1}'] = file_1[key1]
#     for key2 in file_2.keys():
#         if key2 not in file_1.keys():
#             file_3[f'+ {key2}'] = file_2[key2]

#     return json.dumps((file_3), indent=4).replace('"', '')  # str

def generate_diff_for_yaml(filepath1, filepath2):
    """Generate difference files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path_1 = pathlib.Path(dir_path, filepath1)
    file_path_2 = pathlib.Path(dir_path, filepath2)
    file_1 = yaml.load(open(file_path_1), Loader=Loader)   # dict
    file_1 = dict(sorted(file_1.items()))
    file_2 = yaml.load(open(file_path_2), Loader=Loader)
    file_2 = dict(sorted(file_2.items()))
    file_3 = {}

    for key1 in file_1.keys():
        if key1 in file_2.keys():
            if file_1[key1] == file_2[key1]:
                file_3[f"  {key1}"] = file_1[key1]
            else:
                file_3[f"- {key1}"] = file_1[key1]
                file_3[f"+ {key1}"] = file_2[key1]
        else:
            file_3[f'- {key1}'] = file_1[key1]
    for key2 in file_2.keys():
        if key2 not in file_1.keys():
            file_3[f'+ {key2}'] = file_2[key2]
    return json.dumps((file_3), indent=4).replace('"', '')  # str
