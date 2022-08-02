from .Initializer import IMG_INDEX_DICT, replace_windows_characters
from .Settings import *
from .Color import rgb_to_hex_color
from os.path import join, exists
from os import makedirs
import zipfile
import cv2 as opencv
import numpy


def create_indexes(
        show_images: bool,
        write_indexes: bool
):
    print("INFO Start create indexes")
    for img_index_key in IMG_INDEX_DICT:
        img_index_path = IMG_INDEX_DICT[img_index_key][K_INDEX_PATH]
        create_index(show_images, write_indexes, img_index_key, img_index_path)


def create_index(
        show_images: bool,
        write_indexes: bool,
        img_index_key: str,
        img_index_path: str
):
    print(f"     Process index in directory: [{img_index_path}]")
    with open(img_index_path, "w") as index_file:
        for path in IMG_INDEX_DICT[img_index_key][K_PATHS]:
            is_zip = IMG_INDEX_DICT[img_index_key][K_PATHS][path][K_ZIP_FILE_FLAG]
            image_file_dict = IMG_INDEX_DICT[img_index_key][K_PATHS][path][K_IMAGE_FILES]
            path_to_save_index_image = "\\".join(img_index_path.split('\\')[:-1] + [IMG_INDEX_DIR])
            if not exists(path_to_save_index_image) and write_indexes:
                makedirs(path_to_save_index_image)
            process_path(show_images, write_indexes, path, is_zip, image_file_dict, path_to_save_index_image)

            for image_filename in image_file_dict:
                hex_index = image_file_dict[image_filename]
                index_file.write(f"{hex_index}::{join(path, image_filename)}\n")


def process_path(
        show_images: bool,
        write_indexes: bool,
        directory_path: str,
        is_zip: bool,
        image_file_dict: dict,
        path_to_save_index_image: str
):
    number_of_images = len(image_file_dict)
    print(f"      Process path [{directory_path}]{' (ZIP file)' if is_zip else ''} with {number_of_images} images")
    if is_zip:
        with zipfile.ZipFile(directory_path, mode="r") as archive:
            image_counter = 0
            print_progress(number_of_images, image_counter)
            for filename in image_file_dict:
                image_counter += 1
                image_data = archive.read(filename)
                image = opencv.imdecode(numpy.frombuffer(image_data, numpy.uint8), 1)
                print_progress(number_of_images, image_counter)
                hex_index = process_image(
                    show_images,
                    write_indexes,
                    filename,
                    image,
                    path_to_save_index_image,
                    directory_path
                )
                image_file_dict[filename] = hex_index
            print_progress(number_of_images)
    else:
        image_counter = 0
        print_progress(number_of_images, image_counter)
        for filename in image_file_dict:
            image_counter += 1
            filepath = join(directory_path, filename)
            image = opencv.imread(filepath)
            print_progress(number_of_images, image_counter)
            hex_index = process_image(
                show_images,
                write_indexes,
                filename,
                image,
                path_to_save_index_image,
                directory_path
            )
            image_file_dict[filename] = hex_index
        print_progress(number_of_images)


def process_image(
        show_images: bool,
        write_indexes: bool,
        filename: str,
        image: numpy.ndarray,
        path_to_save_index_image: str,
        directory_path: str,
):
    height, width = image.shape[:2]

    original_image_window_name = "Image"
    if show_images:
        if height <= MAX_SHOW_IMAGE_SIZE and width <= MAX_SHOW_IMAGE_SIZE:
            image_to_show = image
            show_size = width, height
        else:
            if width >= height:
                show_size = MAX_SHOW_IMAGE_SIZE, int((height/width) * MAX_SHOW_IMAGE_SIZE)
            else:
                show_size = int((width/height) * MAX_SHOW_IMAGE_SIZE), MAX_SHOW_IMAGE_SIZE
            image_to_show = opencv.resize(image, show_size, interpolation=opencv.INTER_LINEAR)
        original_image_window_name = f"Image [{filename}] [{show_size[0]}x{show_size[1]}]"
        opencv.imshow(original_image_window_name, image_to_show)

    hex_index = ""
    image_index = opencv.resize(image, (INDEX_SIZE, INDEX_SIZE), interpolation=opencv.INTER_LINEAR)
    for row in range(INDEX_SIZE):
        for column in range(INDEX_SIZE):
            blue, green, red = image_index[row, column]
            hex_color = rgb_to_hex_color(red, green, blue)
            hex_index += hex_color

    if write_indexes:
        index_file_name = replace_windows_characters(join(directory_path, filename))
        path_to_save_index_as_image = join(path_to_save_index_image, f"INDEX_{index_file_name}")
        opencv.imwrite(path_to_save_index_as_image, image_index)

    if show_images:
        index_image_window_name = f"Index {INDEX_SIZE} size {INDEX_SIZE*INDEX_SIZE} pixels " \
                                  f"[{filename}] [{show_size[0]}x{show_size[1]}]"
        image_index_image_to_show = opencv.resize(image_index, show_size, interpolation=opencv.INTER_NEAREST)
        opencv.imshow(index_image_window_name, image_index_image_to_show)
        opencv.waitKey(0)
        opencv.destroyWindow(index_image_window_name)
        opencv.destroyWindow(original_image_window_name)

    return hex_index


def print_progress(
        number_of_images: int,
        image_counter: int = None
):
    if image_counter is not None:
        print(PROCESSING_FORMAT_PATTERN.format(
            int((image_counter / number_of_images) * 100),
            image_counter,
            number_of_images,
            ),
            end='',
            flush=True
        )
    else:
        print(END_PROCESSING_FORMAT_PATTERN.format(
            number_of_images
            ),
            flush=True
        )
