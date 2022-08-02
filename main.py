import argparse
import cv2
import os
from Indexer import *


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Image indexer tool")
    arg_parser.add_argument(
        '-c', '--create_index',
        help="Create index hash",
        action="store_true"
    )
    arg_parser.add_argument(
        '-s', '--show_images',
        help="Show images when process",
        action="store_true"
    )
    arg_parser.add_argument(
        '-w', '--write_indexes',
        help="Write generated indexes in index directory",
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
    arg_parser.add_argument(
        '-id', '--index_directory',
        help="Output img index directory (localization of given index created)",
        nargs="?",
        type=str
    )
    parsed_args = arg_parser.parse_args()
    # print(parsed_args)
    initialize_indexer(parsed_args.directory, parsed_args.non_recursive, parsed_args.index_directory)
    if parsed_args.create_index:
        create_indexes(parsed_args.show_images, parsed_args.write_indexes)
    pretty_print()
