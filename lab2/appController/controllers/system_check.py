import platform
import os
from appController.controllers import archive_to_zip


def check_permissions(path_to_folder):
    if os.access(path_to_folder, os.R_OK | os.W_OK):
        return 'no_root'
    else:
        return 'root'


def platform_check():
    os_type = platform.system()

    if os_type == "Windows":
        return "Windows"
    elif os_type == "Linux" or os_type == "Darwin":
        return "Unix"
    else:
        return "Other"


def start_proc(path_to_folder, password):
    system = platform_check()
    permission = check_permissions(path_to_folder)
    result = False

    if permission == 'root':
        if system == 'Windows':
            result = archive_to_zip.windows_with_root(path_to_folder)
        elif system == 'Unix':
            result = archive_to_zip.unix_with_root(path_to_folder, password)
        else:
            print('Error: unknown system!')
    elif permission == 'no_root':
        if system == 'Windows':
            result = archive_to_zip.windows_without_root(path_to_folder)
        elif system == 'Unix':
            result = archive_to_zip.unix_without_root(path_to_folder)
        else:
            print('Error: unknown system!')
    else:
        print('Error: who are you?')

    return result
