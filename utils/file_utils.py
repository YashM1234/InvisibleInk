import os


def is_valid_file(filepath):
    """Checks if the given file exists and is accessible."""
    return os.path.isfile(filepath) and os.access(filepath, os.R_OK)


def get_file_extension(filepath):
    """Returns the file extension in lowercase."""
    return os.path.splitext(filepath)[1].lower()
