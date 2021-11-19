from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80) )
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    category = db.Column(db.String(20))
    image_url = db.Column(db.String(20))

    def __init__(self, name, description, price, category, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image_url = image_url

    def getShortDesc(self):
        if len(self.description) < 10:
            return self.description
        else:
            return self.description[:10] + '...'

    def __repr__(self):
        return str(self.image_url)

def create(name, description, price, category, image_url):
    product = Product(
        name=name, 
        description=description,
        price=price,
        category=category,
        image_url=image_url
    )
    print(f"{name} added successfully")

    db.session.add(product)
    db.session.commit()

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
            Product.query.filter_by(id=pid).update(new_vals)
            db.session.commit()
            print("Product updated successfully")
        else:
            print("Invalid field(s)")
    else:
        print("Product not found")

def deleteSpecific(pid):
    found = Product.query.filter_by(id=pid).first()
    if found:
        db.session.delete(found)
        db.session.commit()
        print("Product deleted successfully")
    else:
        print("Product not found")

def deleteAll():
    if Product.query.first():
        Product.query.delete()
        db.session.commit()
        print("All of the products have been deleted successfully")
    else:
        print("No products found")

def getSpecific(pid):
    found = Product.query.filter_by(id=pid).first()
    print(found)
    if found:
        print("Product found")
    else:
        print("Product not found")
    return found
        
def getAll():
    return Product.query.all()

