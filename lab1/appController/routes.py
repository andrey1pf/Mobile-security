import os

import flask
from flask import render_template, request, redirect, url_for, flash, Flask, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin
from flask import request, jsonify, url_for
import json

from appController import app, check_information

res = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    system_information = check_information.check()
    file_information = {
        'file_name': 'file_name',
        'owner': 'owner',
        'version': 'version'
    }

    select = {
        'res': res
    }

    return render_template('index.html', system_information=system_information, file_information=file_information, select=select), 200


@app.route('/refresh')
def refresh():
    select = {
        'res': 'None'
    }
    file_information = {
        'file_name': 'file_name',
        'owner': 'owner',
        'version': 'version'
    }
    system_information = check_information.check()
    return render_template('index.html', system_information=system_information, file_information=file_information,
                           select=select)


@app.route('/json')
def json():
    system_information = check_information.check()
    return jsonify(system_information)


@app.route('/file', methods=['GET', 'POST'])
def file():
    select = {
        'res': 'None'
    }
    system_information = check_information.check()
    path = '../test'
    if request.method == 'POST':
        path = request.form['path']

    if not os.path.exists(path):
        return render_template('index.html', system_information=system_information, file_information={
            'file_name': 'file_name',
            'owner': 'owner',
            'version': 'version'
        }, select=select)

    file_information = check_information.check_file(path)
    return render_template('index.html', system_information=system_information, file_information=file_information, select=select)


@app.route('/process_menu', methods=['GET', 'POST'])
def process_menu():
    if request.method == 'POST':
        print('de')
    file_information = {
        'file_name': 'file_name',
        'owner': 'owner',
        'version': 'version'
    }
    system_information = check_information.check()
    antivirus = ''
    cpu = ''
    ram = ''

    selected_option = request.form['selectedOption']
    if selected_option == 'as':
        antivirus = system_information.get('Antivirus')
    elif selected_option == 'cpu':
        cpu = system_information.get('CPU')
    else:
        ram = system_information.get('RAM')

    if antivirus:
        select = {
            'res': antivirus
        }
    elif cpu:
        select = {
            'res': cpu
        }
    else:
        select = {
            'res': ram
        }

    global res
    res = select.get('res')
    print(res)

    return redirect(url_for('index'))


'''@app.route('/jsonFile', methods=['GET', 'POST'])
def jsonFile():
    path = '../test'
    if request.method == 'POST':
        path = request.form['path']
    if not os.path.exists(path):
        return jsonify({
            'file_name': 'file_name',
            'owner': 'owner',
            'version': 'version'
        })
    file_information = check_information.check_file(path)
    return jsonify(file_information)'''
