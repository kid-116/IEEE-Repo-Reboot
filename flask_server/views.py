from flask.wrappers import Response
from nlp_search.spell_check_api import spellCheck
from app import app
from models import *
from flask import render_template, request, redirect, stream_with_context, render_template_string
from middlewares import auth
import os
from werkzeug.utils import secure_filename
from nlp_search.string_similarity import sortProducts
from nlp_search.azure_nlp_api import getCategories
import threading
import time
from dotenv import load_dotenv

load_dotenv()

def getCat(cat):
    print(f"Parsing {cat} to be used as a url")
    category = ""
    words = cat.split('-')
    for word in words:
        if word != 'and':
            category += word.capitalize() + " "
        else:
            category += word + " "
    return category[:-1]


def upload_image(image, name):
    print(image, name)
    if image and name:
        image.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(name + '.jpg')))
        print("Image added successfully")
        return name
    else:
        print("No image found")
        return False


@app.route('/products/add', methods=['POST'])
@auth()
def addProduct():
    image_url = upload_image(
        request.files.get('image'),
        request.form.get('name')
    )
    if not image_url:
        image_url = ''
    create(
        request.form.get('name'),
        request.form.get('description'),
        request.form.get('price'),
        request.form.get('category'),
        image_url
    )
    return redirect('/')


@app.route('/products/update/<pid>', methods=['PATCH'])
@auth()
def update(pid):
    if request.form.get('name'):
        name = request.form.get('name')
    else:
        name = getSpecific(pid).name
    updateById(
        pid,
        name=request.form.get('name'),
        description=request.form.get('description'),
        price=request.form.get('price'),
        category=request.form.get('category'),
        image_url=upload_image(
            request.files.get('image'),
            name
        ),
    )
    return redirect('/')


@app.route('/products/delete-all', methods=['DELETE'])
@auth()
def delete():
    deleteAll()
    return redirect('/')


@app.route('/products/delete/<pid>', methods=['DELETE'])
@auth()
def deleteOne(pid):
    deleteSpecific(pid)
    return redirect('/')


@app.route('/products/<pid>', methods=['GET'])
def getOne(pid):
    product = getSpecific(pid)
    return render_template('product.html', product=product)


@app.route('/', methods=['GET'])
def home():
    products = getAll(int(os.getenv('PAGE_LIMIT')))
    return render_template('index.html', products=products, isHomePage=True)


@app.route('/products/categories/<cat>', methods=['GET'])
def getCategory(cat):
    cat = getCat(cat)
    products = getByCategory(cat)
    return render_template('index.html', products=products, isHomePage=False, category=cat)

@app.route('/products/search', methods=["POST"])
def searchProducts():
    isSpellChecked = request.values.get('isSpellChecked')
    query = request.values.get('query')
    if not isSpellChecked:
        new_query = spellCheck(request.values.get('query'))
        if new_query == query:
            isSpellChecked = True

    probableCategories = [None] * 3
    callThread = threading.Thread(target=getCategories, args=(query, probableCategories,))
    callThread.start()

    def generate():
        while callThread.is_alive():
            time.sleep(1)
            # print(':(')
            yield ''
        products = getByCategory(probableCategories)
        products = sortProducts(products, query)
        if not products:
            products = getAll()
            products = sortProducts(products, query)
        if isSpellChecked:
            yield render_template('index.html', products=products, isHomePage=False)
        else:
            yield render_template('index.html', products=products, isHomePage=False, spellCheck=new_query)
    
    return Response(stream_with_context(generate()))

    