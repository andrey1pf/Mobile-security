import hashlib


def hash_file(path_to_filename):
    hash = hashlib.sha1()

    with open(path_to_filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()
