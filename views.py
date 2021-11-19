from app import app
from models import *
from flask import render_template, request, redirect
from middlewares import auth
import os
from werkzeug.utils import secure_filename

def upload_image(request):
    image = request.files['image']
    name = request.form.get('name')
    if image:
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(name + '.jpg')))
        print("Image added successfully")
        return True
    else:
        print("No image found")
        return False

@app.route('/products/add', methods=['POST'])
# @auth()
def addProduct():
    create(
        request.form.get('name'),
        request.form.get('description'),
        request.form.get('price'),
        request.form.get('category'),
        upload_image(request)
    )
    return redirect('/')

@app.route('/products/update/<pid>', methods = ['PATCH'])
# @auth()
def update(pid):
    updateById(
        pid,
        request.forms.get('name'),
        request.forms.get('description'),
        request.forms.get('price'),
        request.forms.get('category'),
        upload_image(request)
    )
    return redirect('/')

@app.route('/products/delete-all', methods=['DELETE'])
# @auth()
def delete():
    deleteAll()
    return redirect('/')

@app.route('/products/delete/<pid>', methods = ['DELETE'])
# @auth()
def deleteOne(pid):
    deleteSpecific(pid)
    return redirect('/')

@app.route('/test', methods=['GET'])
@auth()
def test():
    return 'Hello!'