from Utils import escape_windows_characters, unescape_windows_characters
import unittest


class EscapeWindowsCharactersCase(unittest.TestCase):
    def test_replace_all_wrong_characters(self):
        given = "ABC<>?:'\"123= /|\\**"
        actual = escape_windows_characters(given)
        expected = "ABC=7==8==4==2==6==5=123====_==1==9==0==3==3="
        self.assertEqual(expected, actual)

    def test_replace_all_escaped_characters(self):
        given = "ABC=7==8==4==2==6==5=123====_==1==9==0==3==3="
        actual = unescape_windows_characters(given)
        expected = "ABC<>?:'\"123= /|\\**"
        self.assertEqual(expected, actual)

    def test_escape_windows_path_to_image_index(self):
        given = "H:\\SCRAP_PYTHON\\others.IMG_INDEX"
        actual = escape_windows_characters(given)
        expected = "H=2==0=SCRAP_PYTHON=0=others.IMG_INDEX"
        self.assertEqual(expected, actual)

    def test_unescape_windows_path_to_image_index(self):
        given = "H=2==0=SCRAP_PYTHON=0=others.IMG_INDEX"
        actual = unescape_windows_characters(given)
        expected = "H:\\SCRAP_PYTHON\\others.IMG_INDEX"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
