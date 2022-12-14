import cv2
import os
from os.path import join, isfile
from Indexer import rgb_to_hsv, hsv_to_rgb


IMAGE_PATH = join("F:", "img", "Rilee")
IMAGE_PROCESSED_PATH = join("F:", "img", "processed")


def pixelate_and_save_image(filepath, filename, size):
    image = cv2.imread(filepath)
    height, width = image.shape[:2]
    temp = cv2.resize(image, (size, size), interpolation=cv2.INTER_LINEAR)
    out_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imshow("out", out_image)
    print(f"[{filename}] -> {width}x{height}")
    # cv2.imwrite(join(IMAGE_PROCESSED_PATH, f"out_temp_{filename}"), temp)
    cv2.waitKey(0)


def remap_for_basic_value(filepath, filename):
    image = cv2.imread(filepath)
    height, width = image.shape[:2]
    print(image.shape)
    maximum_pixel_in_sequence = 750
    if height <= maximum_pixel_in_sequence and width <= maximum_pixel_in_sequence:
        height, width = image.shape[:2]
    else:
        if width >= height:
            width, height = maximum_pixel_in_sequence, int((height / width) * maximum_pixel_in_sequence)
        else:
            width, height = int((width / height) * maximum_pixel_in_sequence), maximum_pixel_in_sequence
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

    cv2.imshow("Image", image)
    for row in range(height):
        for column in range(width):
            blue, green, red = image[row, column]
            process = proces_rgb_to_unify_color_map_rgb
            image[row, column] = rgb_to_opencv_format(*process(red, green, blue))
    cv2.imshow("Image unified", image)
    cv2.waitKey()


def rgb_to_opencv_format(red, green, blue):
    return list((blue, green, red))


def proces_rgb_to_desaturate_all_except_hue_range(red, green, blue, goal_hue, goal_hue_range):
    hue, saturation, value = rgb_to_hsv(int(red), int(green), int(blue))


def proces_rgb_to_unify_color_map_rgb(red, green, blue):
    hue, saturation, value = rgb_to_hsv(int(red), int(green), int(blue))
    unified_hue = (int(round(hue / 30)) % 12) * 30
    unified_saturation = int(round(saturation / 10)) * 10
    unified_value = int(round(value / 10)) * 10
    return hsv_to_rgb(unified_hue, unified_saturation, unified_value)


if __name__ == '__main__':
    filename_filepath_tuple_list = list(map(lambda listdir_name: (listdir_name, join(IMAGE_PATH, listdir_name)), os.listdir(IMAGE_PATH)))
    filename_filepath_tuple_list = list(filter(lambda t: isfile(t[1]), filename_filepath_tuple_list))
    filename_filepath_tuple_list = list(filter(lambda t: t[1].split('.')[-1] != 'zip', filename_filepath_tuple_list))
    size = 32
    print(f"Size [{size}] -> dimension {size * size} pixels -> {size * size * 6} hex character")
    for filename, filepath in sorted(filename_filepath_tuple_list, key=lambda x: os.path.getmtime(x[1])):
        # pixelate_and_save_image(filepath, filename, size)
        remap_for_basic_value(filepath, filename)
