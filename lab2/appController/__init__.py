from flask import Flask
import os
import sys

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config.update(
    DEBUG=True
)

if os.geteuid() == 0:
    print("Error: The application must not be run with administrator/root")
    sys.exit(1)

from appController import routes
