import argparse
import cv2
import os
from os.path import join, isfile, isdir
from Indexer import *
import copy
import zipfile

IMG_INDEX_DICT = dict()


def initialize_indexer(arg_directory: list, non_recursive_directory_search: bool):
    print("Initialize indexer")
    for directory in arg_directory:
        path_to_img_index_file = join(directory, "IMGINDEX")
        IMG_INDEX_DICT[path_to_img_index_file] = copy.deepcopy(EMPTY_IMG_INDEX_DICT)
        process_directory(directory, path_to_img_index_file, non_recursive_directory_search)
    print("--summary--")
    for e in IMG_INDEX_DICT:
        print(e)
        for k in IMG_INDEX_DICT[e][K_PATHS]:
            print(f"  {'ZIP ' if IMG_INDEX_DICT[e][K_PATHS][k][K_ZIP_FILE_FLAG] else ''}[{k}]  with {len(IMG_INDEX_DICT[e][K_PATHS][k][K_IMAGE_FILES])} image files")


def process_zip(zip_filename, zip_file_path, path_to_img_index_file):
    add_zip_dir_flag = False
    with zipfile.ZipFile(zip_file_path, mode="r") as archive:
        proper_files_list = list()
        for filename in archive.namelist():
            extension = filename.split(".")[-1]
            if extension in PROPER_IMAGE_FILE_EXTENSIONS:
                proper_files_list.append(filename)
        if len(proper_files_list) > 0:
            add_zip_dir_flag = True
            IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][zip_file_path] = copy.deepcopy(EMPTY_PATH_DICT)
            IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][zip_file_path][K_NAME] = zip_filename
            IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][zip_file_path][K_ZIP_FILE_FLAG] = True
            IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][zip_file_path][K_IMAGE_FILES] = proper_files_list
    return add_zip_dir_flag


def process_directory(directory: str, path_to_img_index_file: str, non_recursive_directory_search: bool):
    print(f"  process directory [{directory}]")
    add_files_flag = False
    file_and_dirs_with_path_list = list(map(lambda listdir_name:
                                        (listdir_name, join(directory, listdir_name), listdir_name.split(".")[-1]),
                                        os.listdir(directory)
                                        ))
    child_directory_list = list()
    zip_file_list = list()
    proper_files_list = list()
    for file_dir_name, path, extension in file_and_dirs_with_path_list:
        if isdir(path):
            if file_dir_name[0] != "." and file_dir_name[:2] != "__":
                child_directory_list.append(path)
        elif isfile(path):
            if extension == "zip":
                zip_file_list.append((file_dir_name, path))
            if extension in PROPER_IMAGE_FILE_EXTENSIONS:
                proper_files_list.append((file_dir_name, path, extension))

    if len(child_directory_list) == 0 and len(zip_file_list) == 0 and len(proper_files_list) == 0:
        print(f"    NONE")
        return False

    directory_name = directory.split("\\")[-1]
    IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory] = copy.deepcopy(EMPTY_PATH_DICT)
    IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory][K_NAME] = directory_name

    if len(proper_files_list) > 0:
        IMG_INDEX_DICT[path_to_img_index_file][K_PATHS][directory][K_IMAGE_FILES] = proper_files_list
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


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Image indexer tool")
    arg_parser.add_argument(
        '-c', '--create_index',
        help="Create index hash",
        action="store_true"
    )
    arg_parser.add_argument(
        '-d', '--directory',
        help="Specify given directory (default os.getcwd)",
        default=[os.getcwd()],
        nargs="+",
        type=str
    )
    arg_parser.add_argument(
        '-n', '--non_recursive',
        help="When used -> only parse files in specific directory (without recursive search in all child directories)",
        action="store_true"
    )
    parsed_args = arg_parser.parse_args()
    print(parsed_args)
    initialize_indexer(parsed_args.directory, parsed_args.non_recursive)
