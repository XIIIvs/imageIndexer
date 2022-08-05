from Color import HTML_COLOR_BANK, BASIC_COLOR_BANK, K_HEX, K_RGB, K_HSV, rgb_to_hex_color, hex_color_to_rgb, rgb_to_hsv, hsv_to_rgb
import unittest


class ColorConversion(unittest.TestCase):
    color_banks = {
        "HTML": HTML_COLOR_BANK,
        "BASIC": BASIC_COLOR_BANK,
    }

    def test_color_banks_duplications(self):
        color_duplication_dict = dict()
        for color_bank_name in self.color_banks:
            color_bank = self.color_banks[color_bank_name]
            print(f"[{color_bank_name}] with {len(color_bank)} colors")
            for color_name in color_bank:
                rgb_color = color_bank[color_name][K_RGB]
                if rgb_color not in color_duplication_dict:
                    color_duplication_dict[rgb_color] = list()
                color_duplication_dict[rgb_color].append(f"{color_bank_name}:{color_name}")
        print()
        for rgb_color, color_name_list in sorted(color_duplication_dict.items(), key=lambda dict_val: len(dict_val[1]), reverse=True):
            print(f"[{len(color_name_list):3}]: {rgb_color} -> {color_name_list}")

    def test_hex_to_rgb_proper_colors(self):
        for color_bank_name in self.color_banks:
            color_bank = self.color_banks[color_bank_name]
            for color_name in color_bank:
                given = color_bank[color_name][K_HEX]
                actual = hex_color_to_rgb(given)
                expected = color_bank[color_name][K_RGB]
                self.assertEqual(expected, actual, f"RGB color [{color_bank_name}:{color_name}] [{given}] "
                                                   f"is not as expected: [{expected}] actual: [{actual}]")

    def test_rgb_to_hex_proper_colors(self):
        for color_bank_name in self.color_banks:
            color_bank = self.color_banks[color_bank_name]
            for color_name in color_bank:
                given = color_bank[color_name][K_RGB]
                actual = rgb_to_hex_color(*given)
                expected = color_bank[color_name][K_HEX]
                self.assertEqual(expected, actual, f"Hex color [{color_bank_name}:{color_name}] [{given}] "
                                                   f"is not as expected: [{expected}] actual: [{actual}]")

    def test_rgb_to_hsv_proper_colors(self):
        for color_bank_name in self.color_banks:
            color_bank = self.color_banks[color_bank_name]
            for color_name in color_bank:
                given = color_bank[color_name][K_RGB]
                actual = rgb_to_hsv(*given)
                expected = color_bank[color_name][K_HSV]
                self.assertEqual(expected, actual, f"HSV color [{color_bank_name}:{color_name}] [{given}] "
                                                   f"is not as expected: [{expected}] actual: [{actual}]")

    def test_hsv_to_rgb_proper_colors(self):
        margin_modifier = (-3, -2, -1, 0, 1)
        for color_bank_name in self.color_banks:
            color_bank = self.color_banks[color_bank_name]
            for color_name in color_bank:
                given = color_bank[color_name][K_HSV]
                actual = hsv_to_rgb(*given)
                expected = color_bank[color_name][K_RGB]
                if expected != actual:
                    for index in range(3):
                        expected_value = expected[index]
                        actual_value = actual[index]
                        self.assertTrue(
                            actual_value in [expected_value - modifier for modifier in margin_modifier],
                            f"RGB color [{color_bank_name}:{color_name}] [{given}] "
                            f"is not as modified expected value: [{expected}] actual: [{actual}] "
                            f"VALUE [{index}] {expected_value} != {actual_value}"
                        )


if __name__ == '__main__':
    unittest.main()
