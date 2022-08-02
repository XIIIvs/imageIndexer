from math import ceil
from typing import Tuple


COLOR_MAX_100 = 100
COLOR_MAX_255 = 255


def validate_var_value(value: int, minimum: int = 0, maximum: int = 255):
    """
    Return value if in range [minimum - maximum] else return corner values
    :param value: value to check
    :param minimum: minimal corner value
    :param maximum: maximal corner value
    :return: value
    """
    return minimum if value < minimum else value if value < maximum else maximum


def hex_color_to_rgb(hex_color) -> Tuple[int, int, int]:
    """
    Get RGB color from hex color string "RRGGBB"
    :param hex_color: str with color code in hex values
    :return: RGB color - red [0-255] green [0-255] blue [0-255]
    """
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex_color(red, green, blue) -> str:
    """
    Get hex color "RRGGBB" from rgb color
    :param red: int [0-255]
    :param green: int [0-255]
    :param blue: int [0-255]
    :return: Hex color string
    """
    def int_val_to_hex_str(val):
        hex_str = str(hex(val))[2:]
        if val < 16:
            hex_str = "0" + hex_str
        return hex_str

    return "{0}{1}{2}".format(int_val_to_hex_str(red), int_val_to_hex_str(green), int_val_to_hex_str(blue))


def rgb_to_hsv(red, green, blue) -> Tuple[int, int, int]:
    """
    Convert red green blue to HSV
    :param red: int [0-255]
    :param green: int [0-255]
    :param blue: int [0-255]
    :return: HSV color - hue [0-255] saturation [0-100] value [0-100]
    """
    c_min = min(red, green, blue)
    c_max = max(red, green, blue)

    hue = 0
    delta = c_max - c_min
    if c_min != c_max:
        if delta == 0:
            hue = 0
        elif red == c_max:
            hue = 0 + ((green - blue) * 60) / delta
        elif green == c_max:
            hue = 120 + ((blue - red) * 60) / delta
        else:
            hue = 240 + ((red - green) * 60) / delta
    hue = hue if hue >= 0 else hue + 360

    saturation = 0
    if c_max != 0:
        saturation = (delta / c_max) * COLOR_MAX_100

    value = (c_max / COLOR_MAX_255) * COLOR_MAX_100

    return int(round(hue)), int(round(saturation)), int(round(value))


def hsv_to_rgb(hue, saturation, value) -> Tuple[int, int, int]:
    """
    Convert hue saturation value to RGB color
    :param hue: int [0-360]
    :param saturation: int [0-100]
    :param value: int [0-100]
    :return: RGB color - red [0-255] green [0-255] blue [0-255]
    """
    h = hue / 60
    s = saturation / COLOR_MAX_100
    v = value / COLOR_MAX_100

    c = v*s
    x = c * (1 - abs(h % 2 - 1))
    m = v-c

    min_val = int(ceil((0 + m) * COLOR_MAX_255))
    med_val = int(ceil((x + m) * COLOR_MAX_255))
    max_val = int(ceil((c + m) * COLOR_MAX_255))

    if 0 <= h <= 1:
        red, green, blue = max_val, med_val, min_val
    elif 1 <= h <= 2:
        red, green, blue = med_val, max_val, min_val
    elif 2 <= h <= 3:
        red, green, blue = min_val, max_val, med_val
    elif 3 <= h <= 4:
        red, green, blue = min_val, med_val, max_val
    elif 4 <= h <= 5:
        red, green, blue = med_val, min_val, max_val
    else:
        red, green, blue = max_val, min_val, med_val

    red = validate_var_value(red, maximum=COLOR_MAX_255)
    green = validate_var_value(green, maximum=COLOR_MAX_255)
    blue = validate_var_value(blue, maximum=COLOR_MAX_255)

    return red, green, blue


if __name__ == '__main__':
    # VALS R 146 G 156 B 145 -> (1511, 7, 61)
    print(rgb_to_hsv(151, 154, 159))
