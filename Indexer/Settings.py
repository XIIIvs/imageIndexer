MAX_SHOW_IMAGE_SIZE = 1000
INDEX_SIZE = 32

PROCESSING_FORMAT_PATTERN = "\r        PROCESSING [{0:>3}%] {1:>6} / {2}"
END_PROCESSING_FORMAT_PATTERN = "\r        DONE       [100%] {0:>6} / {0}"

PROPER_IMAGE_FILE_EXTENSIONS = (
    "png",
    "jpg",
    "jpeg",
    "bmp"
)

IMG_INDEX_EXTENSION = "IMG_INDEX"
IMG_INDEX = f".{IMG_INDEX_EXTENSION}"
IMG_INDEX_DIR = f".{IMG_INDEX_EXTENSION}_DIR"

K_PATHS = "paths"
K_IMAGE_FILES = "image_files"
K_NAME = "name"
K_ZIP_FILE_FLAG = "zip_file_flag"
K_INDEX_PATH = "index_path"

EMPTY_IMG_INDEX_DICT = {
    K_PATHS: dict(),
    K_INDEX_PATH: str()
}

EMPTY_PATH_DICT = {
    K_NAME: str(),
    K_ZIP_FILE_FLAG: bool(),
    K_IMAGE_FILES: dict()
}
