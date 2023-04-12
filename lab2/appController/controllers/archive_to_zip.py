import ctypes
import shutil
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
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", "archive_to_zip.py", None, 1)
    shutil.make_archive(get_archive_name(path), "zip", path)
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
