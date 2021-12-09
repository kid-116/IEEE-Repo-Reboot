from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='static')
# run_with_ngrok(app)

# db configuration
db_name = 'easybuy.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run()
