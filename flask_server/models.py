from app import db
from sqlalchemy import func
from dotenv import load_dotenv
from sqlalchemy import exc
import os

load_dotenv()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(20), nullable=False)

    def __init__(self, name, description, price, category, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image_url = image_url

    def getShortName(self):
        if len(self.name) < int(os.getenv('SHORT_TITLE_LEN')):
            return self.name
        else:
            return self.name[:int(os.getenv('SHORT_TITLE_LEN'))] + '...'

    def __repr__(self):
        return str(self.name)


def create(name, description, price, category, image_url):
    product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        image_url=image_url
    )
    try:
        db.session.add(product)
        db.session.commit()
        
    except exc.SQLAlchemyError as e:
        print(e)


def updateById(pid, **kwargs):
    print(kwargs)
    found = Product.query.filter_by(id=pid).first()
    if found:
        new_vals = {}
        fields = ["name", "description", "price", "category", "image_url"]
        for field in fields:
            data = kwargs[field]
            if data:
                new_vals[field] = data

        if new_vals:
            try:
                Product.query.filter_by(id=pid).update(new_vals)
                db.session.commit()
            except exc.SQLAlchemyError as e:
                print(e)
            print(f"Product {pid} updated successfully")
        else:
            print("No new values found!")
    else:
        print("Product with id {pid} not found")


def deleteSpecific(pid):
    found = Product.query.filter_by(id=pid).first()
    if found:
        db.session.delete(found)
        db.session.commit()
        print(f"Product {pid} deleted successfully")
    else:
        print(f"Product with id {pid} not found")


def deleteAll():
    if Product.query.first():
        Product.query.delete()
        db.session.commit()
        print("All of the products have been deleted successfully")
    else:
        print("No products found")


def getSpecific(pid):
    found = Product.query.filter_by(id=pid).first()
    if found:
        print(f"Product {pid} found")
    else:
        print(f"Product with id {pid} not found")
    return found


def getAll(size=-1):
    if size == -1:
        return Product.query.all()
    else:
        return Product.query.order_by(func.random()).limit(size).all()


def getByCategory(cats):
    found = Product.query.filter(Product.category.in_(cats)).all()
    if found:
        print(f"Products found in {cats}")
    else:
        print(f"No product found in {cats}")
    return found


def getCategories():
    found = Product.query.all()
    if found:
        return [prod.category for prod in found]
    else:
        print("No products found")
    return None
