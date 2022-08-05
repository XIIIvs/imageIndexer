from math import ceil
from typing import Tuple


COLOR_MAX_100 = 100
COLOR_MAX_255 = 255

K_HEX = "hex"
K_RGB = "rgb"
K_HSV = "hsv"

HTML_COLOR_BANK = {
        "AliceBlue": {K_HEX: "f0f8ff", K_RGB: (240, 248, 255), K_HSV: (208, 6, 100)},
        "AntiqueWhite": {K_HEX: "faebd7", K_RGB: (250, 235, 215), K_HSV: (34, 14, 98)},
        "Aqua": {K_HEX: "00ffff", K_RGB: (0, 255, 255), K_HSV: (180, 100, 100)},
        "Aquamarine": {K_HEX: "7fffd4", K_RGB: (127, 255, 212), K_HSV: (160, 50, 100)},
        "Azure": {K_HEX: "f0ffff", K_RGB: (240, 255, 255), K_HSV: (180, 6, 100)},
        "Beige": {K_HEX: "f5f5dc", K_RGB: (245, 245, 220), K_HSV: (60, 10, 96)},
        "Bisque": {K_HEX: "ffe4c4", K_RGB: (255, 228, 196), K_HSV: (33, 23, 100)},
        "Black": {K_HEX: "000000", K_RGB: (0, 0, 0), K_HSV: (0, 0, 0)},
        "BlanchedAlmond": {K_HEX: "ffebcd", K_RGB: (255, 235, 205), K_HSV: (36, 20, 100)},
        "Blue": {K_HEX: "0000ff", K_RGB: (0, 0, 255), K_HSV: (240, 100, 100)},
        "BlueViolet": {K_HEX: "8a2be2", K_RGB: (138, 43, 226), K_HSV: (271, 81, 89)},
        "Brown": {K_HEX: "a52a2a", K_RGB: (165, 42, 42), K_HSV: (0, 75, 65)},
        "BurlyWood": {K_HEX: "deb887", K_RGB: (222, 184, 135), K_HSV: (34, 39, 87)},
        "CadetBlue": {K_HEX: "5f9ea0", K_RGB: (95, 158, 160), K_HSV: (182, 41, 63)},
        "Chartreuse": {K_HEX: "7fff00", K_RGB: (127, 255, 0), K_HSV: (90, 100, 100)},
        "Chocolate": {K_HEX: "d2691e", K_RGB: (210, 105, 30), K_HSV: (25, 86, 82)},
        "Coral": {K_HEX: "ff7f50", K_RGB: (255, 127, 80), K_HSV: (16, 69, 100)},
        "CornflowerBlue": {K_HEX: "6495ed", K_RGB: (100, 149, 237), K_HSV: (219, 58, 93)},
        "Cornsilk": {K_HEX: "fff8dc", K_RGB: (255, 248, 220), K_HSV: (48, 14, 100)},
        "Crimson": {K_HEX: "dc143c", K_RGB: (220, 20, 60), K_HSV: (348, 91, 86)},
        "Cyan": {K_HEX: "00ffff", K_RGB: (0, 255, 255), K_HSV: (180, 100, 100)},
        "DarkBlue": {K_HEX: "00008b", K_RGB: (0, 0, 139), K_HSV: (240, 100, 55)},
        "DarkCyan": {K_HEX: "008b8b", K_RGB: (0, 139, 139), K_HSV: (180, 100, 55)},
        "DarkGoldenRod": {K_HEX: "b8860b", K_RGB: (184, 134, 11), K_HSV: (43, 94, 72)},
        "DarkGrey": {K_HEX: "a9a9a9", K_RGB: (169, 169, 169), K_HSV: (0, 0, 66)},
        "DarkGreen": {K_HEX: "006400", K_RGB: (0, 100, 0), K_HSV: (120, 100, 39)},
        "DarkKhaki": {K_HEX: "bdb76b", K_RGB: (189, 183, 107), K_HSV: (56, 43, 74)},
        "DarkMagenta": {K_HEX: "8b008b", K_RGB: (139, 0, 139), K_HSV: (300, 100, 55)},
        "DarkOliveGreen": {K_HEX: "556b2f", K_RGB: (85, 107, 47), K_HSV: (82, 56, 42)},
        "Darkorange": {K_HEX: "ff8c00", K_RGB: (255, 140, 0), K_HSV: (33, 100, 100)},
        "DarkOrchid": {K_HEX: "9932cc", K_RGB: (153, 50, 204), K_HSV: (280, 75, 80)},
        "DarkRed": {K_HEX: "8b0000", K_RGB: (139, 0, 0), K_HSV: (0, 100, 55)},
        "DarkSalmon": {K_HEX: "e9967a", K_RGB: (233, 150, 122), K_HSV: (15, 48, 91)},
        "DarkSeaGreen": {K_HEX: "8fbc8f", K_RGB: (143, 188, 143), K_HSV: (120, 24, 74)},
        "DarkSlateBlue": {K_HEX: "483d8b", K_RGB: (72, 61, 139), K_HSV: (248, 56, 55)},
        "DarkSlateGrey": {K_HEX: "2f4f4f", K_RGB: (47, 79, 79), K_HSV: (180, 41, 31)},
        "DarkTurquoise": {K_HEX: "00ced1", K_RGB: (0, 206, 209), K_HSV: (181, 100, 82)},
        "DarkViolet": {K_HEX: "9400d3", K_RGB: (148, 0, 211), K_HSV: (282, 100, 83)},
        "DeepPink": {K_HEX: "ff1493", K_RGB: (255, 20, 147), K_HSV: (328, 92, 100)},
        "DeepSkyBlue": {K_HEX: "00bfff", K_RGB: (0, 191, 255), K_HSV: (195, 100, 100)},
        "DimGray": {K_HEX: "696969", K_RGB: (105, 105, 105), K_HSV: (0, 0, 41)},
        "DodgerBlue": {K_HEX: "1e90ff", K_RGB: (30, 144, 255), K_HSV: (210, 88, 100)},
        "FireBrick": {K_HEX: "b22222", K_RGB: (178, 34, 34), K_HSV: (0, 81, 70)},
        "FloralWhite": {K_HEX: "fffaf0", K_RGB: (255, 250, 240), K_HSV: (40, 6, 100)},
        "ForestGreen": {K_HEX: "228b22", K_RGB: (34, 139, 34), K_HSV: (120, 76, 55)},
        "Fuchsia": {K_HEX: "ff00ff", K_RGB: (255, 0, 255), K_HSV: (300, 100, 100)},
        "Gainsboro": {K_HEX: "dcdcdc", K_RGB: (220, 220, 220), K_HSV: (0, 0, 86)},
        "GhostWhite": {K_HEX: "f8f8ff", K_RGB: (248, 248, 255), K_HSV: (240, 3, 100)},
        "Gold": {K_HEX: "ffd700", K_RGB: (255, 215, 0), K_HSV: (51, 100, 100)},
        "GoldenRod": {K_HEX: "daa520", K_RGB: (218, 165, 32), K_HSV: (43, 85, 85)},
        "Grey": {K_HEX: "808080", K_RGB: (128, 128, 128), K_HSV: (0, 0, 50)},
        "Green": {K_HEX: "008000", K_RGB: (0, 128, 0), K_HSV: (120, 100, 50)},
        "GreenYellow": {K_HEX: "adff2f", K_RGB: (173, 255, 47), K_HSV: (84, 82, 100)},
        "HoneyDew": {K_HEX: "f0fff0", K_RGB: (240, 255, 240), K_HSV: (120, 6, 100)},
        "HotPink": {K_HEX: "ff69b4", K_RGB: (255, 105, 180), K_HSV: (330, 59, 100)},
        "IndianRed": {K_HEX: "cd5c5c", K_RGB: (205, 92, 92), K_HSV: (0, 55, 80)},
        "Indigo": {K_HEX: "4b0082", K_RGB: (75, 0, 130), K_HSV: (275, 100, 51)},
        "Ivory": {K_HEX: "fffff0", K_RGB: (255, 255, 240), K_HSV: (60, 6, 100)},
        "Khaki": {K_HEX: "f0e68c", K_RGB: (240, 230, 140), K_HSV: (54, 42, 94)},
        "Lavender": {K_HEX: "e6e6fa", K_RGB: (230, 230, 250), K_HSV: (240, 8, 98)},
        "LavenderBlush": {K_HEX: "fff0f5", K_RGB: (255, 240, 245), K_HSV: (340, 6, 100)},
        "LawnGreen": {K_HEX: "7cfc00", K_RGB: (124, 252, 0), K_HSV: (90, 100, 99)},
        "LemonChiffon": {K_HEX: "fffacd", K_RGB: (255, 250, 205), K_HSV: (54, 20, 100)},
        "LightBlue": {K_HEX: "add8e6", K_RGB: (173, 216, 230), K_HSV: (195, 25, 90)},
        "LightCoral": {K_HEX: "f08080", K_RGB: (240, 128, 128), K_HSV: (0, 47, 94)},
        "LightCyan": {K_HEX: "e0ffff", K_RGB: (224, 255, 255), K_HSV: (180, 12, 100)},
        "LightGoldenRodYellow": {K_HEX: "fafad2", K_RGB: (250, 250, 210), K_HSV: (60, 16, 98)},
        "LightGrey": {K_HEX: "d3d3d3", K_RGB: (211, 211, 211), K_HSV: (0, 0, 83)},
        "LightGreen": {K_HEX: "90ee90", K_RGB: (144, 238, 144), K_HSV: (120, 39, 93)},
        "LightPink": {K_HEX: "ffb6c1", K_RGB: (255, 182, 193), K_HSV: (351, 29, 100)},
        "LightSalmon": {K_HEX: "ffa07a", K_RGB: (255, 160, 122), K_HSV: (17, 52, 100)},
        "LightSeaGreen": {K_HEX: "20b2aa", K_RGB: (32, 178, 170), K_HSV: (177, 82, 70)},
        "LightSkyBlue": {K_HEX: "87cefa", K_RGB: (135, 206, 250), K_HSV: (203, 46, 98)},
        "LightSlateGrey": {K_HEX: "778899", K_RGB: (119, 136, 153), K_HSV: (210, 22, 60)},
        "LightSteelBlue": {K_HEX: "b0c4de", K_RGB: (176, 196, 222), K_HSV: (214, 21, 87)},
        "LightYellow": {K_HEX: "ffffe0", K_RGB: (255, 255, 224), K_HSV: (60, 12, 100)},
        "Lime": {K_HEX: "00ff00", K_RGB: (0, 255, 0), K_HSV: (120, 100, 100)},
        "LimeGreen": {K_HEX: "32cd32", K_RGB: (50, 205, 50), K_HSV: (120, 76, 80)},
        "Linen": {K_HEX: "faf0e6", K_RGB: (250, 240, 230), K_HSV: (30, 8, 98)},
        "Magenta": {K_HEX: "ff00ff", K_RGB: (255, 0, 255), K_HSV: (300, 100, 100)},
        "Maroon": {K_HEX: "800000", K_RGB: (128, 0, 0), K_HSV: (0, 100, 50)},
        "MediumAquaMarine": {K_HEX: "66cdaa", K_RGB: (102, 205, 170), K_HSV: (160, 50, 80)},
        "MediumBlue": {K_HEX: "0000cd", K_RGB: (0, 0, 205), K_HSV: (240, 100, 80)},
        "MediumOrchid": {K_HEX: "ba55d3", K_RGB: (186, 85, 211), K_HSV: (288, 60, 83)},
        "MediumPurple": {K_HEX: "9370d8", K_RGB: (147, 112, 216), K_HSV: (260, 48, 85)},
        "MediumSeaGreen": {K_HEX: "3cb371", K_RGB: (60, 179, 113), K_HSV: (147, 66, 70)},
        "MediumSlateBlue": {K_HEX: "7b68ee", K_RGB: (123, 104, 238), K_HSV: (249, 56, 93)},
        "MediumSpringGreen": {K_HEX: "00fa9a", K_RGB: (0, 250, 154), K_HSV: (157, 100, 98)},
        "MediumTurquoise": {K_HEX: "48d1cc", K_RGB: (72, 209, 204), K_HSV: (178, 66, 82)},
        "MediumVioletRed": {K_HEX: "c71585", K_RGB: (199, 21, 133), K_HSV: (322, 89, 78)},
        "MidnightBlue": {K_HEX: "191970", K_RGB: (25, 25, 112), K_HSV: (240, 78, 44)},
        "MintCream": {K_HEX: "f5fffa", K_RGB: (245, 255, 250), K_HSV: (150, 4, 100)},
        "MistyRose": {K_HEX: "ffe4e1", K_RGB: (255, 228, 225), K_HSV: (6, 12, 100)},
        "Moccasin": {K_HEX: "ffe4b5", K_RGB: (255, 228, 181), K_HSV: (38, 29, 100)},
        "NavajoWhite": {K_HEX: "ffdead", K_RGB: (255, 222, 173), K_HSV: (36, 32, 100)},
        "Navy": {K_HEX: "000080", K_RGB: (0, 0, 128), K_HSV: (240, 100, 50)},
        "OldLace": {K_HEX: "fdf5e6", K_RGB: (253, 245, 230), K_HSV: (39, 9, 99)},
        "Olive": {K_HEX: "808000", K_RGB: (128, 128, 0), K_HSV: (60, 100, 50)},
        "OliveDrab": {K_HEX: "6b8e23", K_RGB: (107, 142, 35), K_HSV: (80, 75, 56)},
        "Orange": {K_HEX: "ffa500", K_RGB: (255, 165, 0), K_HSV: (39, 100, 100)},
        "OrangeRed": {K_HEX: "ff4500", K_RGB: (255, 69, 0), K_HSV: (16, 100, 100)},
        "Orchid": {K_HEX: "da70d6", K_RGB: (218, 112, 214), K_HSV: (302, 49, 85)},
        "PaleGoldenRod": {K_HEX: "eee8aa", K_RGB: (238, 232, 170), K_HSV: (55, 29, 93)},
        "PaleGreen": {K_HEX: "98fb98", K_RGB: (152, 251, 152), K_HSV: (120, 39, 98)},
        "PaleTurquoise": {K_HEX: "afeeee", K_RGB: (175, 238, 238), K_HSV: (180, 26, 93)},
        "PaleVioletRed": {K_HEX: "d87093", K_RGB: (216, 112, 147), K_HSV: (340, 48, 85)},
        "PapayaWhip": {K_HEX: "ffefd5", K_RGB: (255, 239, 213), K_HSV: (37, 16, 100)},
        "PeachPuff": {K_HEX: "ffdab9", K_RGB: (255, 218, 185), K_HSV: (28, 27, 100)},
        "Peru": {K_HEX: "cd853f", K_RGB: (205, 133, 63), K_HSV: (30, 69, 80)},
        "Pink": {K_HEX: "ffc0cb", K_RGB: (255, 192, 203), K_HSV: (350, 25, 100)},
        "Plum": {K_HEX: "dda0dd", K_RGB: (221, 160, 221), K_HSV: (300, 28, 87)},
        "PowderBlue": {K_HEX: "b0e0e6", K_RGB: (176, 224, 230), K_HSV: (187, 23, 90)},
        "Purple": {K_HEX: "800080", K_RGB: (128, 0, 128), K_HSV: (300, 100, 50)},
        "Red": {K_HEX: "ff0000", K_RGB: (255, 0, 0), K_HSV: (0, 100, 100)},
        "RosyBrown": {K_HEX: "bc8f8f", K_RGB: (188, 143, 143), K_HSV: (0, 24, 74)},
        "RoyalBlue": {K_HEX: "4169e1", K_RGB: (65, 105, 225), K_HSV: (225, 71, 88)},
        "SaddleBrown": {K_HEX: "8b4513", K_RGB: (139, 69, 19), K_HSV: (25, 86, 55)},
        "Salmon": {K_HEX: "fa8072", K_RGB: (250, 128, 114), K_HSV: (6, 54, 98)},
        "SandyBrown": {K_HEX: "f4a460", K_RGB: (244, 164, 96), K_HSV: (28, 61, 96)},
        "SeaGreen": {K_HEX: "2e8b57", K_RGB: (46, 139, 87), K_HSV: (146, 67, 55)},
        "SeaShell": {K_HEX: "fff5ee", K_RGB: (255, 245, 238), K_HSV: (25, 7, 100)},
        "Sienna": {K_HEX: "a0522d", K_RGB: (160, 82, 45), K_HSV: (19, 72, 63)},
        "Silver": {K_HEX: "c0c0c0", K_RGB: (192, 192, 192), K_HSV: (0, 0, 75)},
        "SkyBlue": {K_HEX: "87ceeb", K_RGB: (135, 206, 235), K_HSV: (197, 43, 92)},
        "SlateBlue": {K_HEX: "6a5acd", K_RGB: (106, 90, 205), K_HSV: (248, 56, 80)},
        "SlateGrey": {K_HEX: "708090", K_RGB: (112, 128, 144), K_HSV: (210, 22, 56)},
        "Snow": {K_HEX: "fffafa", K_RGB: (255, 250, 250), K_HSV: (0, 2, 100)},
        "SpringGreen": {K_HEX: "00ff7f", K_RGB: (0, 255, 127), K_HSV: (150, 100, 100)},
        "SteelBlue": {K_HEX: "4682b4", K_RGB: (70, 130, 180), K_HSV: (207, 61, 71)},
        "Tan": {K_HEX: "d2b48c", K_RGB: (210, 180, 140), K_HSV: (34, 33, 82)},
        "Teal": {K_HEX: "008080", K_RGB: (0, 128, 128), K_HSV: (180, 100, 50)},
        "Thistle": {K_HEX: "d8bfd8", K_RGB: (216, 191, 216), K_HSV: (300, 12, 85)},
        "Tomato": {K_HEX: "ff6347", K_RGB: (255, 99, 71), K_HSV: (9, 72, 100)},
        "Turquoise": {K_HEX: "40e0d0", K_RGB: (64, 224, 208), K_HSV: (174, 71, 88)},
        "Violet": {K_HEX: "ee82ee", K_RGB: (238, 130, 238), K_HSV: (300, 45, 93)},
        "Wheat": {K_HEX: "f5deb3", K_RGB: (245, 222, 179), K_HSV: (39, 27, 96)},
        "White": {K_HEX: "ffffff", K_RGB: (255, 255, 255), K_HSV: (0, 0, 100)},
        "WhiteSmoke": {K_HEX: "f5f5f5", K_RGB: (245, 245, 245), K_HSV: (0, 0, 96)},
        "Yellow": {K_HEX: "ffff00", K_RGB: (255, 255, 0), K_HSV: (60, 100, 100)},
        "YellowGreen": {K_HEX: "9acd32", K_RGB: (154, 205, 50), K_HSV: (80, 76, 80)},
}

BASIC_COLOR_BANK = {
    "White": {K_HEX: "ffffff", K_RGB: (255, 255, 255), K_HSV: (0, 0, 100)},
    "LightGrey": {K_HEX: "c0c0c0", K_RGB: (192, 192, 192), K_HSV: (0, 0, 75)},
    "Grey": {K_HEX: "808080", K_RGB: (128, 128, 128), K_HSV: (0, 0, 50)},
    "DarkGrey": {K_HEX: "404040", K_RGB: (64, 64, 64), K_HSV: (0, 0, 25)},
    "Black": {K_HEX: "000000", K_RGB: (0, 0, 0), K_HSV: (0, 0, 0)},
    "Red": {K_HEX: "ff0000", K_RGB: (255, 0, 0), K_HSV: (0, 100, 100)},
    "Orange": {K_HEX: "ff8000", K_RGB: (255, 128, 0), K_HSV: (30, 100, 100)},
    "Yellow": {K_HEX: "ffff00", K_RGB: (255, 255, 0), K_HSV: (60, 100, 100)},
    "Lime": {K_HEX: "80ff00", K_RGB: (128, 255, 0), K_HSV: (90, 100, 100)},
    "Green": {K_HEX: "00ff00", K_RGB: (0, 255, 0), K_HSV: (120, 100, 100)},
    "SeaGreen": {K_HEX: "00ff80", K_RGB: (0, 255, 128), K_HSV: (150, 100, 100)},
    "Cyan": {K_HEX: "00ffff", K_RGB: (0, 255, 255), K_HSV: (180, 100, 100)},
    "SkyBlue": {K_HEX: "0080ff", K_RGB: (0, 128, 255), K_HSV: (210, 100, 100)},
    "Blue": {K_HEX: "0000ff", K_RGB: (0, 0, 255), K_HSV: (240, 100, 100)},
    "Purple": {K_HEX: "8000ff", K_RGB: (128, 0, 255), K_HSV: (270, 100, 100)},
    "Magenta": {K_HEX: "ff00ff", K_RGB: (255, 0, 255), K_HSV: (300, 100, 100)},
    "Rose": {K_HEX: "ff0080", K_RGB: (255, 0, 128), K_HSV: (330, 100, 100)},
    "Shaded Red": {K_HEX: "c00000", K_RGB: (192, 0, 0), K_HSV: (0, 100, 75)},
    "Shaded Orange": {K_HEX: "c06000", K_RGB: (192, 96, 0), K_HSV: (30, 100, 75)},
    "Shaded Yellow": {K_HEX: "c0c000", K_RGB: (192, 192, 0), K_HSV: (60, 100, 75)},
    "Shaded Lime": {K_HEX: "60c000", K_RGB: (96, 192, 0), K_HSV: (90, 100, 75)},
    "Shaded Green": {K_HEX: "00c000", K_RGB: (0, 192, 0), K_HSV: (120, 100, 75)},
    "Shaded SeaGreen": {K_HEX: "00c060", K_RGB: (0, 192, 96), K_HSV: (150, 100, 75)},
    "Shaded Cyan": {K_HEX: "00c0c0", K_RGB: (0, 192, 192), K_HSV: (180, 100, 75)},
    "Shaded SkyBlue": {K_HEX: "0060c0", K_RGB: (0, 96, 192), K_HSV: (210, 100, 75)},
    "Shaded Blue": {K_HEX: "0000c0", K_RGB: (0, 0, 192), K_HSV: (240, 100, 75)},
    "Shaded Purple": {K_HEX: "6000c0", K_RGB: (96, 0, 192), K_HSV: (270, 100, 75)},
    "Shaded Magenta": {K_HEX: "c000c0", K_RGB: (192, 0, 192), K_HSV: (300, 100, 75)},
    "Shaded Rose": {K_HEX: "c00060", K_RGB: (192, 0, 96), K_HSV: (330, 100, 75)},
    "Medium Red": {K_HEX: "800000", K_RGB: (128, 0, 0), K_HSV: (0, 100, 50)},
    "Medium Orange": {K_HEX: "804000", K_RGB: (128, 64, 0), K_HSV: (30, 100, 50)},
    "Medium Yellow": {K_HEX: "808000", K_RGB: (128, 128, 0), K_HSV: (60, 100, 50)},
    "Medium Lime": {K_HEX: "408000", K_RGB: (64, 128, 0), K_HSV: (90, 100, 50)},
    "Medium Green": {K_HEX: "008000", K_RGB: (0, 128, 0), K_HSV: (120, 100, 50)},
    "Medium SeaGreen": {K_HEX: "008040", K_RGB: (0, 128, 64), K_HSV: (150, 100, 50)},
    "Medium Cyan": {K_HEX: "008080", K_RGB: (0, 128, 128), K_HSV: (180, 100, 50)},
    "Medium SkyBlue": {K_HEX: "004080", K_RGB: (0, 64, 128), K_HSV: (210, 100, 50)},
    "Medium Blue": {K_HEX: "000080", K_RGB: (0, 0, 128), K_HSV: (240, 100, 50)},
    "Medium Purple": {K_HEX: "400080", K_RGB: (64, 0, 128), K_HSV: (270, 100, 50)},
    "Medium Magenta": {K_HEX: "800080", K_RGB: (128, 0, 128), K_HSV: (300, 100, 50)},
    "Medium Rose": {K_HEX: "800040", K_RGB: (128, 0, 64), K_HSV: (330, 100, 50)},
    "Dark Red": {K_HEX: "400000", K_RGB: (64, 0, 0), K_HSV: (0, 100, 25)},
    "Dark Orange": {K_HEX: "402000", K_RGB: (64, 32, 0), K_HSV: (30, 100, 25)},
    "Dark Yellow": {K_HEX: "404000", K_RGB: (64, 64, 0), K_HSV: (60, 100, 25)},
    "Dark Lime": {K_HEX: "204000", K_RGB: (32, 64, 0), K_HSV: (90, 100, 25)},
    "Dark Green": {K_HEX: "004000", K_RGB: (0, 64, 0), K_HSV: (120, 100, 25)},
    "Dark SeaGreen": {K_HEX: "004020", K_RGB: (0, 64, 32), K_HSV: (150, 100, 25)},
    "Dark Cyan": {K_HEX: "004040", K_RGB: (0, 64, 64), K_HSV: (180, 100, 25)},
    "Dark SkyBlue": {K_HEX: "002040", K_RGB: (0, 32, 64), K_HSV: (210, 100, 25)},
    "Dark Blue": {K_HEX: "000040", K_RGB: (0, 0, 64), K_HSV: (240, 100, 25)},
    "Dark Purple": {K_HEX: "200040", K_RGB: (32, 0, 64), K_HSV: (270, 100, 25)},
    "Dark Magenta": {K_HEX: "400040", K_RGB: (64, 0, 64), K_HSV: (300, 100, 25)},
    "Dark Rose": {K_HEX: "400020", K_RGB: (64, 0, 32), K_HSV: (330, 100, 25)},
    "Layered Red": {K_HEX: "ff4040", K_RGB: (255, 64, 64), K_HSV: (0, 75, 100)},
    "Layered Orange": {K_HEX: "ffa040", K_RGB: (255, 160, 64), K_HSV: (30, 75, 100)},
    "Layered Yellow": {K_HEX: "ffff40", K_RGB: (255, 255, 64), K_HSV: (60, 75, 100)},
    "Layered Lime": {K_HEX: "a0ff40", K_RGB: (160, 255, 64), K_HSV: (90, 75, 100)},
    "Layered Green": {K_HEX: "40ff40", K_RGB: (64, 255, 64), K_HSV: (120, 75, 100)},
    "Layered SeaGreen": {K_HEX: "40ffa0", K_RGB: (64, 255, 160), K_HSV: (150, 75, 100)},
    "Layered Cyan": {K_HEX: "40ffff", K_RGB: (64, 255, 255), K_HSV: (180, 75, 100)},
    "Layered SkyBlue": {K_HEX: "40a0ff", K_RGB: (64, 160, 255), K_HSV: (210, 75, 100)},
    "Layered Blue": {K_HEX: "4040ff", K_RGB: (64, 64, 255), K_HSV: (240, 75, 100)},
    "Layered Purple": {K_HEX: "a040ff", K_RGB: (160, 64, 255), K_HSV: (270, 75, 100)},
    "Layered Magenta": {K_HEX: "ff40ff", K_RGB: (255, 64, 255), K_HSV: (300, 75, 100)},
    "Layered Rose": {K_HEX: "ff40a0", K_RGB: (255, 64, 160), K_HSV: (330, 75, 100)},
    "Shaded Layered Red": {K_HEX: "c03030", K_RGB: (192, 48, 48), K_HSV: (0, 75, 75)},
    "Shaded Layered Orange": {K_HEX: "c07830", K_RGB: (192, 120, 48), K_HSV: (30, 75, 75)},
    "Shaded Layered Yellow": {K_HEX: "c0c030", K_RGB: (192, 192, 48), K_HSV: (60, 75, 75)},
    "Shaded Layered Lime": {K_HEX: "78c030", K_RGB: (120, 192, 48), K_HSV: (90, 75, 75)},
    "Shaded Layered Green": {K_HEX: "30c030", K_RGB: (48, 192, 48), K_HSV: (120, 75, 75)},
    "Shaded Layered SeaGreen": {K_HEX: "30c078", K_RGB: (48, 192, 120), K_HSV: (150, 75, 75)},
    "Shaded Layered Cyan": {K_HEX: "30c0c0", K_RGB: (48, 192, 192), K_HSV: (180, 75, 75)},
    "Shaded Layered SkyBlue": {K_HEX: "3078c0", K_RGB: (48, 120, 192), K_HSV: (210, 75, 75)},
    "Shaded Layered Blue": {K_HEX: "3030c0", K_RGB: (48, 48, 192), K_HSV: (240, 75, 75)},
    "Shaded Layered Purple": {K_HEX: "7830c0", K_RGB: (120, 48, 192), K_HSV: (270, 75, 75)},
    "Shaded Layered Magenta": {K_HEX: "c030c0", K_RGB: (192, 48, 192), K_HSV: (300, 75, 75)},
    "Shaded Layered Rose": {K_HEX: "c03078", K_RGB: (192, 48, 120), K_HSV: (330, 75, 75)},
    "Medium Layered Red": {K_HEX: "802020", K_RGB: (128, 32, 32), K_HSV: (0, 75, 50)},
    "Medium Layered Orange": {K_HEX: "805020", K_RGB: (128, 80, 32), K_HSV: (30, 75, 50)},
    "Medium Layered Yellow": {K_HEX: "808020", K_RGB: (128, 128, 32), K_HSV: (60, 75, 50)},
    "Medium Layered Lime": {K_HEX: "508020", K_RGB: (80, 128, 32), K_HSV: (90, 75, 50)},
    "Medium Layered Green": {K_HEX: "208020", K_RGB: (32, 128, 32), K_HSV: (120, 75, 50)},
    "Medium Layered SeaGreen": {K_HEX: "208050", K_RGB: (32, 128, 80), K_HSV: (150, 75, 50)},
    "Medium Layered Cyan": {K_HEX: "208080", K_RGB: (32, 128, 128), K_HSV: (180, 75, 50)},
    "Medium Layered SkyBlue": {K_HEX: "205080", K_RGB: (32, 80, 128), K_HSV: (210, 75, 50)},
    "Medium Layered Blue": {K_HEX: "202080", K_RGB: (32, 32, 128), K_HSV: (240, 75, 50)},
    "Medium Layered Purple": {K_HEX: "502080", K_RGB: (80, 32, 128), K_HSV: (270, 75, 50)},
    "Medium Layered Magenta": {K_HEX: "802080", K_RGB: (128, 32, 128), K_HSV: (300, 75, 50)},
    "Medium Layered Rose": {K_HEX: "802050", K_RGB: (128, 32, 80), K_HSV: (330, 75, 50)},
    "Dark Layered Red": {K_HEX: "401010", K_RGB: (64, 16, 16), K_HSV: (0, 75, 25)},
    "Dark Layered Orange": {K_HEX: "402810", K_RGB: (64, 40, 16), K_HSV: (30, 75, 25)},
    "Dark Layered Yellow": {K_HEX: "404010", K_RGB: (64, 64, 16), K_HSV: (60, 75, 25)},
    "Dark Layered Lime": {K_HEX: "284010", K_RGB: (40, 64, 16), K_HSV: (90, 75, 25)},
    "Dark Layered Green": {K_HEX: "104010", K_RGB: (16, 64, 16), K_HSV: (120, 75, 25)},
    "Dark Layered SeaGreen": {K_HEX: "104028", K_RGB: (16, 64, 40), K_HSV: (150, 75, 25)},
    "Dark Layered Cyan": {K_HEX: "104040", K_RGB: (16, 64, 64), K_HSV: (180, 75, 25)},
    "Dark Layered SkyBlue": {K_HEX: "102840", K_RGB: (16, 40, 64), K_HSV: (210, 75, 25)},
    "Dark Layered Blue": {K_HEX: "101040", K_RGB: (16, 16, 64), K_HSV: (240, 75, 25)},
    "Dark Layered Purple": {K_HEX: "281040", K_RGB: (40, 16, 64), K_HSV: (270, 75, 25)},
    "Dark Layered Magenta": {K_HEX: "401040", K_RGB: (64, 16, 64), K_HSV: (300, 75, 25)},
    "Dark Layered Rose": {K_HEX: "401028", K_RGB: (64, 16, 40), K_HSV: (330, 75, 25)},
    "Toned Red": {K_HEX: "ff8080", K_RGB: (255, 128, 128), K_HSV: (0, 50, 100)},
    "Toned Orange": {K_HEX: "ffc080", K_RGB: (255, 192, 128), K_HSV: (30, 50, 100)},
    "Toned Yellow": {K_HEX: "ffff80", K_RGB: (255, 255, 128), K_HSV: (60, 50, 100)},
    "Toned Lime": {K_HEX: "c0ff80", K_RGB: (192, 255, 128), K_HSV: (90, 50, 100)},
    "Toned Green": {K_HEX: "80ff80", K_RGB: (128, 255, 128), K_HSV: (120, 50, 100)},
    "Toned SeaGreen": {K_HEX: "80ffc0", K_RGB: (128, 255, 192), K_HSV: (150, 50, 100)},
    "Toned Cyan": {K_HEX: "80ffff", K_RGB: (128, 255, 255), K_HSV: (180, 50, 100)},
    "Toned SkyBlue": {K_HEX: "80c0ff", K_RGB: (128, 192, 255), K_HSV: (210, 50, 100)},
    "Toned Blue": {K_HEX: "8080ff", K_RGB: (128, 128, 255), K_HSV: (240, 50, 100)},
    "Toned Purple": {K_HEX: "c080ff", K_RGB: (192, 128, 255), K_HSV: (270, 50, 100)},
    "Toned Magenta": {K_HEX: "ff80ff", K_RGB: (255, 128, 255), K_HSV: (300, 50, 100)},
    "Toned Rose": {K_HEX: "ff80c0", K_RGB: (255, 128, 192), K_HSV: (330, 50, 100)},
    "Shaded Toned Red": {K_HEX: "c06060", K_RGB: (192, 96, 96), K_HSV: (0, 50, 75)},
    "Shaded Toned Orange": {K_HEX: "c09060", K_RGB: (192, 144, 96), K_HSV: (30, 50, 75)},
    "Shaded Toned Yellow": {K_HEX: "c0c060", K_RGB: (192, 192, 96), K_HSV: (60, 50, 75)},
    "Shaded Toned Lime": {K_HEX: "90c060", K_RGB: (144, 192, 96), K_HSV: (90, 50, 75)},
    "Shaded Toned Green": {K_HEX: "60c060", K_RGB: (96, 192, 96), K_HSV: (120, 50, 75)},
    "Shaded Toned SeaGreen": {K_HEX: "60c090", K_RGB: (96, 192, 144), K_HSV: (150, 50, 75)},
    "Shaded Toned Cyan": {K_HEX: "60c0c0", K_RGB: (96, 192, 192), K_HSV: (180, 50, 75)},
    "Shaded Toned SkyBlue": {K_HEX: "6090c0", K_RGB: (96, 144, 192), K_HSV: (210, 50, 75)},
    "Shaded Toned Blue": {K_HEX: "6060c0", K_RGB: (96, 96, 192), K_HSV: (240, 50, 75)},
    "Shaded Toned Purple": {K_HEX: "9060c0", K_RGB: (144, 96, 192), K_HSV: (270, 50, 75)},
    "Shaded Toned Magenta": {K_HEX: "c060c0", K_RGB: (192, 96, 192), K_HSV: (300, 50, 75)},
    "Shaded Toned Rose": {K_HEX: "c06090", K_RGB: (192, 96, 144), K_HSV: (330, 50, 75)},
    "Medium Toned Red": {K_HEX: "804040", K_RGB: (128, 64, 64), K_HSV: (0, 50, 50)},
    "Medium Toned Orange": {K_HEX: "806040", K_RGB: (128, 96, 64), K_HSV: (30, 50, 50)},
    "Medium Toned Yellow": {K_HEX: "808040", K_RGB: (128, 128, 64), K_HSV: (60, 50, 50)},
    "Medium Toned Lime": {K_HEX: "608040", K_RGB: (96, 128, 64), K_HSV: (90, 50, 50)},
    "Medium Toned Green": {K_HEX: "408040", K_RGB: (64, 128, 64), K_HSV: (120, 50, 50)},
    "Medium Toned SeaGreen": {K_HEX: "408060", K_RGB: (64, 128, 96), K_HSV: (150, 50, 50)},
    "Medium Toned Cyan": {K_HEX: "408080", K_RGB: (64, 128, 128), K_HSV: (180, 50, 50)},
    "Medium Toned SkyBlue": {K_HEX: "406080", K_RGB: (64, 96, 128), K_HSV: (210, 50, 50)},
    "Medium Toned Blue": {K_HEX: "404080", K_RGB: (64, 64, 128), K_HSV: (240, 50, 50)},
    "Medium Toned Purple": {K_HEX: "604080", K_RGB: (96, 64, 128), K_HSV: (270, 50, 50)},
    "Medium Toned Magenta": {K_HEX: "804080", K_RGB: (128, 64, 128), K_HSV: (300, 50, 50)},
    "Medium Toned Rose": {K_HEX: "804060", K_RGB: (128, 64, 96), K_HSV: (330, 50, 50)},
    "Dark Toned Red": {K_HEX: "402020", K_RGB: (64, 32, 32), K_HSV: (0, 50, 25)},
    "Dark Toned Orange": {K_HEX: "403020", K_RGB: (64, 48, 32), K_HSV: (30, 50, 25)},
    "Dark Toned Yellow": {K_HEX: "404020", K_RGB: (64, 64, 32), K_HSV: (60, 50, 25)},
    "Dark Toned Lime": {K_HEX: "304020", K_RGB: (48, 64, 32), K_HSV: (90, 50, 25)},
    "Dark Toned Green": {K_HEX: "204020", K_RGB: (32, 64, 32), K_HSV: (120, 50, 25)},
    "Dark Toned SeaGreen": {K_HEX: "204030", K_RGB: (32, 64, 48), K_HSV: (150, 50, 25)},
    "Dark Toned Cyan": {K_HEX: "204040", K_RGB: (32, 64, 64), K_HSV: (180, 50, 25)},
    "Dark Toned SkyBlue": {K_HEX: "203040", K_RGB: (32, 48, 64), K_HSV: (210, 50, 25)},
    "Dark Toned Blue": {K_HEX: "202040", K_RGB: (32, 32, 64), K_HSV: (240, 50, 25)},
    "Dark Toned Purple": {K_HEX: "302040", K_RGB: (48, 32, 64), K_HSV: (270, 50, 25)},
    "Dark Toned Magenta": {K_HEX: "402040", K_RGB: (64, 32, 64), K_HSV: (300, 50, 25)},
    "Dark Toned Rose": {K_HEX: "402030", K_RGB: (64, 32, 48), K_HSV: (330, 50, 25)},
    "Desaturated Red": {K_HEX: "ffc0c0", K_RGB: (255, 192, 192), K_HSV: (0, 25, 100)},
    "Desaturated Orange": {K_HEX: "ffe0c0", K_RGB: (255, 224, 192), K_HSV: (30, 25, 100)},
    "Desaturated Yellow": {K_HEX: "ffffc0", K_RGB: (255, 255, 192), K_HSV: (60, 25, 100)},
    "Desaturated Lime": {K_HEX: "e0ffc0", K_RGB: (224, 255, 192), K_HSV: (90, 25, 100)},
    "Desaturated Green": {K_HEX: "c0ffc0", K_RGB: (192, 255, 192), K_HSV: (120, 25, 100)},
    "Desaturated SeaGreen": {K_HEX: "c0ffe0", K_RGB: (192, 255, 224), K_HSV: (150, 25, 100)},
    "Desaturated Cyan": {K_HEX: "c0ffff", K_RGB: (192, 255, 255), K_HSV: (180, 25, 100)},
    "Desaturated SkyBlue": {K_HEX: "c0e0ff", K_RGB: (192, 224, 255), K_HSV: (210, 25, 100)},
    "Desaturated Blue": {K_HEX: "c0c0ff", K_RGB: (192, 192, 255), K_HSV: (240, 25, 100)},
    "Desaturated Purple": {K_HEX: "e0c0ff", K_RGB: (224, 192, 255), K_HSV: (270, 25, 100)},
    "Desaturated Magenta": {K_HEX: "ffc0ff", K_RGB: (255, 192, 255), K_HSV: (300, 25, 100)},
    "Desaturated Rose": {K_HEX: "ffc0e0", K_RGB: (255, 192, 224), K_HSV: (330, 25, 100)},
    "Shaded Desaturated Red": {K_HEX: "c09090", K_RGB: (192, 144, 144), K_HSV: (0, 25, 75)},
    "Shaded Desaturated Orange": {K_HEX: "c0a890", K_RGB: (192, 168, 144), K_HSV: (30, 25, 75)},
    "Shaded Desaturated Yellow": {K_HEX: "c0c090", K_RGB: (192, 192, 144), K_HSV: (60, 25, 75)},
    "Shaded Desaturated Lime": {K_HEX: "a8c090", K_RGB: (168, 192, 144), K_HSV: (90, 25, 75)},
    "Shaded Desaturated Green": {K_HEX: "90c090", K_RGB: (144, 192, 144), K_HSV: (120, 25, 75)},
    "Shaded Desaturated SeaGreen": {K_HEX: "90c0a8", K_RGB: (144, 192, 168), K_HSV: (150, 25, 75)},
    "Shaded Desaturated Cyan": {K_HEX: "90c0c0", K_RGB: (144, 192, 192), K_HSV: (180, 25, 75)},
    "Shaded Desaturated SkyBlue": {K_HEX: "90a8c0", K_RGB: (144, 168, 192), K_HSV: (210, 25, 75)},
    "Shaded Desaturated Blue": {K_HEX: "9090c0", K_RGB: (144, 144, 192), K_HSV: (240, 25, 75)},
    "Shaded Desaturated Purple": {K_HEX: "a890c0", K_RGB: (168, 144, 192), K_HSV: (270, 25, 75)},
    "Shaded Desaturated Magenta": {K_HEX: "c090c0", K_RGB: (192, 144, 192), K_HSV: (300, 25, 75)},
    "Shaded Desaturated Rose": {K_HEX: "c090a8", K_RGB: (192, 144, 168), K_HSV: (330, 25, 75)},
    "Medium Desaturated Red": {K_HEX: "806060", K_RGB: (128, 96, 96), K_HSV: (0, 25, 50)},
    "Medium Desaturated Orange": {K_HEX: "807060", K_RGB: (128, 112, 96), K_HSV: (30, 25, 50)},
    "Medium Desaturated Yellow": {K_HEX: "808060", K_RGB: (128, 128, 96), K_HSV: (60, 25, 50)},
    "Medium Desaturated Lime": {K_HEX: "708060", K_RGB: (112, 128, 96), K_HSV: (90, 25, 50)},
    "Medium Desaturated Green": {K_HEX: "608060", K_RGB: (96, 128, 96), K_HSV: (120, 25, 50)},
    "Medium Desaturated SeaGreen": {K_HEX: "608070", K_RGB: (96, 128, 112), K_HSV: (150, 25, 50)},
    "Medium Desaturated Cyan": {K_HEX: "608080", K_RGB: (96, 128, 128), K_HSV: (180, 25, 50)},
    "Medium Desaturated SkyBlue": {K_HEX: "607080", K_RGB: (96, 112, 128), K_HSV: (210, 25, 50)},
    "Medium Desaturated Blue": {K_HEX: "606080", K_RGB: (96, 96, 128), K_HSV: (240, 25, 50)},
    "Medium Desaturated Purple": {K_HEX: "706080", K_RGB: (112, 96, 128), K_HSV: (270, 25, 50)},
    "Medium Desaturated Magenta": {K_HEX: "806080", K_RGB: (128, 96, 128), K_HSV: (300, 25, 50)},
    "Medium Desaturated Rose": {K_HEX: "806070", K_RGB: (128, 96, 112), K_HSV: (330, 25, 50)},
    "Dark Desaturated Red": {K_HEX: "403030", K_RGB: (64, 48, 48), K_HSV: (0, 25, 25)},
    "Dark Desaturated Orange": {K_HEX: "403830", K_RGB: (64, 56, 48), K_HSV: (30, 25, 25)},
    "Dark Desaturated Yellow": {K_HEX: "404030", K_RGB: (64, 64, 48), K_HSV: (60, 25, 25)},
    "Dark Desaturated Lime": {K_HEX: "384030", K_RGB: (56, 64, 48), K_HSV: (90, 25, 25)},
    "Dark Desaturated Green": {K_HEX: "304030", K_RGB: (48, 64, 48), K_HSV: (120, 25, 25)},
    "Dark Desaturated SeaGreen": {K_HEX: "304038", K_RGB: (48, 64, 56), K_HSV: (150, 25, 25)},
    "Dark Desaturated Cyan": {K_HEX: "304040", K_RGB: (48, 64, 64), K_HSV: (180, 25, 25)},
    "Dark Desaturated SkyBlue": {K_HEX: "303840", K_RGB: (48, 56, 64), K_HSV: (210, 25, 25)},
    "Dark Desaturated Blue": {K_HEX: "303040", K_RGB: (48, 48, 64), K_HSV: (240, 25, 25)},
    "Dark Desaturated Purple": {K_HEX: "383040", K_RGB: (56, 48, 64), K_HSV: (270, 25, 25)},
    "Dark Desaturated Magenta": {K_HEX: "403040", K_RGB: (64, 48, 64), K_HSV: (300, 25, 25)},
    "Dark Desaturated Rose": {K_HEX: "403038", K_RGB: (64, 48, 56), K_HSV: (330, 25, 25)},
}


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
