# @ Import *
from flask import Flask 

app = Flask(__name__)


app.config.from_pyfile('setting.py')


# # Import Blueprint 
from dbapi.api import api as HomeAPI
from dbapp.app import app as HomeApp

app.register_blueprint(HomeApp)
app.register_blueprint(HomeAPI,url_prefix='/api/')
