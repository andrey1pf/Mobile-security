import zipfile
import os
from pathlib import Path


def get_archive_name(path):
    last_slash_index = path.rfind("/")
    if last_slash_index != len(path) - 1:
        name = path[last_slash_index + 1:]
    else:
        path = path[:len(path) - 1]
        last_slash_index = path.rfind("/")
        name = path[last_slash_index + 1:]

    return name


def windows_with_root(path):
    with zipfile.ZipFile(get_archive_name(path), 'w') as zipf:
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, path))
    path = Path(path + '.zip')
    return path.is_file()


def windows_without_root(path):
    operation = f"powershell Compress-Archive {path} {path}.zip"
    os.system(operation)
    path = Path(path + '.zip')
    return path.is_file()


def unix_with_root(path, password):
    operation = f"echo {password} | sudo -S zip -r {path} {path}"
    os.system(operation)
    path = Path(path + '.zip')
    return path.is_file()


def unix_without_root(path):
    operation = f"zip -r {path} {path}"
    os.system(operation)
    path = Path(path + '.zip')
    return path.is_file()
