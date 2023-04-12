from PIL import Image


def get_name(path):
    index = path.rfind(".")
    if index != len(path) - 1:
        name = path[:index]
    else:
        path = path[:len(path) - 1]
        index = path.rfind(".")
        name = path[:index]

    return name


def convert_to_png(path_to_file):
    image = Image.open(path_to_file)
    image = image.convert('RGB')
    image.save(f"{get_name(path_to_file)}.png")
