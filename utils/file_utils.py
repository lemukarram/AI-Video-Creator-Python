# utils/file_utils.py
import os

def ensure_dir(path):
    """
    Creates a folder if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
