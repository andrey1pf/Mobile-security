from flask import render_template
from flask import request

from appController import app
from appController.controllers import calculate_hash, convert_to_png, system_check

message_zip = {
    "info": ''
}

message_hash = {
    "info": '',
    "hash": '',
}

message_png = {
    "info": '',
    "png": ''
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path_to_folder = request.form['file_path']
        if system_check.check_permissions(path_to_folder) == 'root':
            try:
                password = request.form['password_input']
                if system_check.start_proc(path_to_folder, password):
                    message_zip["info"] = f'Archive was successfully saved in {path_to_folder}'
                else:
                    message_zip["info"] = f'Check your password'
            except:
                message_zip["info"] = f'Folder {path_to_folder} was not found...'
        else:
            try:
                system_check.start_proc(path_to_folder, '0')
                message_zip["info"] = f'Archive was successfully saved in {path_to_folder}'
            except:
                message_zip["info"] = f'Folder {path_to_folder} was not found...'

    message_png.clear()
    message_hash.clear()
    return render_template('index.html', message_zip=message_zip, message_hash=message_hash, message_png=message_png)


@app.route("/check_hash", methods=['GET', 'POST'])
def check_hash():
    if request.method == 'POST':
        path_to_folder = request.form['file_path']
        try:
            hash_value = calculate_hash.hash_file(path_to_folder)
            message_hash["hash"] = hash_value
            message_hash["info"] = ''
        except:
            message_hash["hash"] = ''
            message_hash["info"] = f'File {path_to_folder} was not found...'

    message_png.clear()
    message_zip.clear()
    return render_template("index.html", message_zip=message_zip, message_hash=message_hash, message_png=message_png)


@app.route("/convert", methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        path_to_file = request.form['file_path']
        try:
            convert_to_png.convert_to_png(path_to_file)
            message_png["png"] = 'File was successfully convert in the same directory'
            message_png["info"] = ''
        except:
            message_png["png"] = ''
            message_png["info"] = f'We have some problems with your file'

    message_zip.clear()
    message_hash.clear()
    return render_template("index.html", message_zip=message_zip, message_hash=message_hash, message_png=message_png)

