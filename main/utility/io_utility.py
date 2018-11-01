import json
import os
from os import path
from main import MAIN_ROOT_DIR, DEMO_ROOT_DIR, TEST_ROOT_DIR, ROOT_DIR


def read_dictionary_from_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()
        return json.loads("".join(lines))


def write_dictionary_to_file(dictionary, filepath):
    with open(filepath, "w") as f:
        f.write(json.dumps(dictionary, indent=4))


def standardize_path(path_string):
    path_string = path_string.strip()
    path_string = path_string.replace("\\", "/")
    return path_string


def __get_relative_path(relative_to, relative_path):
    relative_path = standardize_path(relative_path)
    return standardize_path(os.path.join(relative_to, relative_path))


def get_project_path(relative_path):
    return __get_relative_path(ROOT_DIR, relative_path)

def get_main_path(relative_path):
    return __get_relative_path(MAIN_ROOT_DIR, relative_path)

