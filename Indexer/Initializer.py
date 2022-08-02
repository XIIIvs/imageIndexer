from .Settings import *
import os
import copy
import zipfile
from os.path import join, isfile, isdir


IMG_INDEX_DICT = dict()
PATHS = dict()


def initialize_indexer(
        arg_directory: list,
        non_recursive_directory_search: bool,
        fixed_index_path: str = None
):
    print("INFO Initialize indexer")
    for directory in arg_directory:
        path_to_img_index_file = join(directory, IMG_INDEX)
        IMG_INDEX_DICT[path_to_img_index_file] = copy.deepcopy(EMPTY_IMG_INDEX_DICT)
        IMG_INDEX_DICT[path_to_img_index_file][K_INDEX_PATH] = \
            path_to_img_index_file \
            if fixed_index_path is None \
            else join(fixed_index_path, f"{replace_windows_characters(directory)}{IMG_INDEX}")
        process_directory(directory, path_to_img_index_file, non_recursive_directory_search)


def process_zip(
        zip_filename: str,
        zip_file_path: str,
        path_to_img_index_file: str
):
    with zipfile.ZipFile(zip_file_path, mode="r") as archive:
        proper_files_dict = dict()
        for filename in archive.namelist():
            extension = filename.split(".")[-1]
            if extension in PROPER_IMAGE_FILE_EXTENSIONS:
                proper_files_dict[filename] = None
        if len(proper_files_dict) > 0:
            add_directory_to_img_index(path_to_img_index_file, zip_file_path, zip_filename, True)
            IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][zip_file_path][K_IMAGE_FILES] = proper_files_dict


def process_directory(
        directory: str,
        path_to_img_index_file: str,
        non_recursive_directory_search: bool
):
    print(f"     Process directory [{directory}]")
    add_files_flag = False
    file_and_dirs_with_path_list = list(map(lambda listdir_name:
                                            (listdir_name, join(directory, listdir_name), listdir_name.split(".")[-1]),
                                            os.listdir(directory)
                                            ))
    child_directory_list = list()
    zip_file_list = list()
    proper_files_dict = dict()
    for file_dir_name, path, extension in file_and_dirs_with_path_list:
        if isdir(path):
            if file_dir_name[0] != "." and file_dir_name[:2] != "__":
                child_directory_list.append(path)
        elif isfile(path):
            if extension == "zip":
                zip_file_list.append((file_dir_name, path))
            if extension in PROPER_IMAGE_FILE_EXTENSIONS:
                proper_files_dict[file_dir_name] = None

    if len(child_directory_list) == 0 and len(zip_file_list) == 0 and len(proper_files_dict) == 0:
        return False

    directory_name = directory.split("\\")[-1]
    add_directory_to_img_index(path_to_img_index_file, directory, directory_name)

    if len(proper_files_dict) > 0:
        IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory][K_IMAGE_FILES] = proper_files_dict
        add_files_flag = True

    if len(zip_file_list) > 0:
        for zip_filename, zip_file_path in zip_file_list:
            process_zip(zip_filename, zip_file_path, path_to_img_index_file)

    if not non_recursive_directory_search:
        for child_directory in child_directory_list:
            add_directory = process_directory(child_directory, path_to_img_index_file, non_recursive_directory_search)
            add_files_flag = add_files_flag or add_directory

    if not add_files_flag:
        IMG_INDEX_DICT[path_to_img_index_file][K_PATHS].pop(directory)
    return add_files_flag


def add_directory_to_img_index(
        path_to_img_index_file: str,
        directory_key: str,
        directory_name: str,
        zip_flag: bool = False
):
    if directory_key in PATHS:
        print_warn(f"Given path [{directory_key}] "
                   f"already exists in other img index"
                   f" - check -> {PATHS[directory_key]} vs {path_to_img_index_file}")
    IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory_key] = copy.deepcopy(EMPTY_PATH_DICT)
    IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory_key][K_NAME] = directory_name
    IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory_key][K_ZIP_FILE_FLAG] = zip_flag
    PATHS[directory_key] = path_to_img_index_file


def print_warn(msg: str):
    print(f"\n----\nWARN {msg}\n----\n")


def replace_windows_characters(string: str):
    return string \
        .replace(" ", "-") \
        .replace("\\", "-") \
        .replace("/", "-") \
        .replace(":", "") \
        .replace("*", "") \
        .replace("?", "") \
        .replace('"', "") \
        .replace("'", "") \
        .replace("<", "") \
        .replace(">", "") \
        .replace("|", "")


def pretty_print():
    print("Summary for IMG INDEX DICT")
    for img_index_path in IMG_INDEX_DICT:
        print(f" - index [{img_index_path}] -> {IMG_INDEX_DICT[img_index_path][K_INDEX_PATH]}")
        for path in IMG_INDEX_DICT[img_index_path][K_PATHS]:
            name = IMG_INDEX_DICT[img_index_path][K_PATHS][path][K_NAME]
            files = IMG_INDEX_DICT[img_index_path][K_PATHS][path][K_IMAGE_FILES]
            is_zip = IMG_INDEX_DICT[img_index_path][K_PATHS][path][K_ZIP_FILE_FLAG]
            print(f" --- path {'ZIP' if is_zip else '   '} [{path}] - '{name}' - with {len(files)} image files")
            for filename in files:
                hex_index = files[filename]
                if hex_index is not None:
                    print(f"   --- file [{filename}] indexed >{hex_index[:60]}...<")
