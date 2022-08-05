MAX_SHOW_IMAGE_SIZE = 1000
INDEX_SIZE = 16

PROCESSING_FORMAT_PATTERN = "\r        PROCESSING [{0:>3}%] {1:>6} / {2}"
END_PROCESSING_FORMAT_PATTERN = "\r        DONE       [100%] {0:>6} / {0}"

PROPER_IMAGE_FILE_EXTENSIONS = (
    "png",
    "jpg",
    "jpeg",
    "bmp",
    "gif",
)

IMG_INDEX_EXTENSION = "IMG_INDEX"
IMG_INDEX = f".{IMG_INDEX_EXTENSION}"
IMG_INDEX_DIR = f".{IMG_INDEX_EXTENSION}_DIR"

K_PATHS = "paths"
K_IMAGE_FILES = "image_files"
K_NAME = "name"
K_ZIP_FILE_FLAG = "zip_file_flag"
K_INDEX_PATH = "index_path"
K_CREATED_FLAG = "created_in_this_run"

EMPTY_IMG_INDEX_DICT = {
    K_PATHS: dict(),
    K_INDEX_PATH: str(),
    K_CREATED_FLAG: bool()
}

EMPTY_PATH_DICT = {
    K_NAME: str(),
    K_ZIP_FILE_FLAG: bool(),
    K_IMAGE_FILES: dict()
}

IMG_INDEX_DICT = dict()
PATHS = dict()


def escape_windows_characters(string: str):
    return string\
        .replace("=", "===")\
        .replace(" ", "=_=")\
        .replace("\\", "=0=")\
        .replace("/", "=1=")\
        .replace(":", "=2=")\
        .replace("*", "=3=")\
        .replace("?", "=4=")\
        .replace('"', "=5=")\
        .replace("'", "=6=")\
        .replace("<", "=7=")\
        .replace(">", "=8=")\
        .replace("|", "=9=")


def unescape_windows_characters(string: str):
    return string\
        .replace("=9=", "|")\
        .replace("=8=", ">")\
        .replace("=7=", "<")\
        .replace("=6=", "'")\
        .replace("=5=", '"')\
        .replace("=4=", "?")\
        .replace("=3=", "*")\
        .replace("=2=", ":")\
        .replace("=1=", "/")\
        .replace("=0=", "\\")\
        .replace("=_=", " ")\
        .replace("===", "=")
