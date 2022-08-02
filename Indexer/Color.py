import logging
from math import ceil
from typing import Tuple, Optional


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


class Color:
    def __init__(
            self,
            hex_color: str = None,
            rgb: Tuple[int, int, int] = None,
            hsv: Tuple[int, int, int] = None,
            alpha: Optional[int] = 255,
            color: 'Color' = None
    ):
        self.logger = logging.getLogger("graphic.Color")
        self.alpha: int = alpha

        if color is not None:
            self.hex_color = color.hex_color
            self.red = color.red
            self.green = color.green
            self.blue = color.blue
            self.hue = color.hue
            self.saturation = color.saturation
            self.value = color.value
            self.alpha = color.alpha

        elif hex_color is not None:
            if len(hex_color) != 6:
                raise ValueError("Hex color should have 6 characters")

            self.hex_color = hex_color
            self.red, self.green, self.blue = hex_color_to_rgb(self.hex_color)
            self.hue, self.saturation, self.value = rgb_to_hsv(self.red, self.green, self.blue)

        elif rgb is not None:
            self.red = validate_var_value(rgb[0], maximum=COLOR_MAX_255)
            self.green = validate_var_value(rgb[1], maximum=COLOR_MAX_255)
            self.blue = validate_var_value(rgb[2], maximum=COLOR_MAX_255)
            self.hue, self.saturation, self.value = rgb_to_hsv(self.red, self.green, self.blue)
            self.hex_color = rgb_to_hex_color(self.red, self.green, self.blue)

        elif hsv is not None:
            self.hue = validate_var_value(hsv[0], maximum=359)
            self.saturation = validate_var_value(hsv[1], maximum=100)
            self.value = validate_var_value(hsv[2], maximum=100)
            self.red, self.green, self.blue = hsv_to_rgb(self.hue, self.saturation, self.value)
            self.hex_color = rgb_to_hex_color(self.red, self.green, self.blue)

        else:
            self.hex_color = "000000"
            self.red: int = 0
            self.green: int = 0
            self.blue: int = 0
            self.hue: int = 0
            self.saturation: int = 0
            self.value: int = 0

        if self.saturation == 0 or self.value == 0:
            self.hue = 0

    def __repr__(self) -> str:
        return "<color '{7}' RGB ({0}, {1}, {2}) HSV ({3}, {4}, {5}) A {6}>".format(
            self.red,
            self.green,
            self.blue,
            self.hue,
            self.saturation,
            self.value,
            self.alpha,
            self.hex_color
        )

    def __eq__(self, other: 'Color') -> bool:
        return self.red == other.red \
               and self.green == other.green \
               and self.blue == other.blue \
               and self.alpha == other.alpha

    def get_modified_color(
            self,
            mod_red: int = 0,
            mod_green: int = 0,
            mod_blue: int = 0,
            mod_hue: int = 0,
            mod_saturation: int = 0,
            mod_value: int = 0,
            mod_alpha: int = 0
    ) -> 'Color':
        new_alpha = validate_var_value(self.alpha + mod_alpha, maximum=255)

        new_red = validate_var_value(self.red + mod_red, maximum=255)
        new_green = validate_var_value(self.green + mod_green, maximum=255)
        new_blue = validate_var_value(self.blue + mod_blue, maximum=255)

        new_color = Color(rgb=(new_red, new_green, new_blue), alpha=new_alpha)

        if not (mod_hue == 0 and mod_saturation == 0 and mod_value == 0):
            new_hue, new_saturation, new_value = new_color.get_hsv()

            new_hue += mod_hue
            new_hue = new_hue % 360

            new_saturation = validate_var_value(new_saturation + mod_saturation, maximum=100)
            new_value = validate_var_value(new_value + mod_value, maximum=100)

            new_color = Color(hsv=(new_hue, new_saturation, new_value), alpha=new_alpha)

        return new_color

    def get_rgb(self) -> Tuple[int, int, int]:
        """
        :return: RGB color tuple (red [0-255], green [0-255], blue [0-255])
        """
        return self.red, self.green, self.blue

    def get_rgba(self) -> Tuple[int, int, int, int]:
        """
        :return: RGBA color tuple (red [0-255], green [0-255], blue [0-255], alpha [0-255])
        """
        return self.red, self.green, self.blue, self.alpha

    def get_hsv(self) -> Tuple[int, int, int]:
        """
        :return: HSV color tuple (hue [0-255], saturation [0-255], value [0-255])
        """
        return self.hue, self.saturation, self.value

    def get_hsva(self) -> Tuple[int, int, int, int]:
        """
        :return: HSVA color tuple (hue [0-255], saturation [0-255], value [0-255], alpha [0-255])
        """
        return self.hue, self.saturation, self.value, self.alpha


if __name__ == '__main__':
    # VALS R 146 G 156 B 145 -> (1511, 7, 61)
    print(rgb_to_hsv(151, 154, 159))
