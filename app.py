from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='static')

# db configuration
db_name = 'easybuy.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
db = SQLAlchemy(app)

from views import *

@app.route('/', methods=['GET'])
def home():
    products = getAll()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    db.create_all()
    app.run()