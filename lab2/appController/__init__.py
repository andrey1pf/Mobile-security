from flask import Flask
import os
import sys
import ctypes

from appController.controllers import system_check

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config.update(
    DEBUG=True
)

system = system_check.platform_check()
if system == 'Windows':
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("Error: The application must not be run with administrator/root")
        sys.exit(1)
else:
    if os.geteuid() == 0:
        print("Error: The application must not be run with administrator/root")
        sys.exit(1)

from appController import routes
