from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80) )
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    category = db.Column(db.String(20))

    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def getShortDesc(self):
        if len(self.desc < 10):
            return self.desc
        else:
            return self.desc[:10] + '...'

    def __repr__(self):
        return str(self.name)

def create(name, description, price, category, image_provided):
    product = Product(
        name=name, 
        description=description,
        price=price,
        category=category,
    )
    print(f"{name} added successfully")

    db.session.add(product)
    db.session.commit()

def updateById(pid, **kwargs):
    found = Product.query.filter_by(id= pid).first()
    if found:
        new_vals = {}
        fields = ["name", "description", "price", "category", "image_updated"]
        for field in fields:
            data = kwargs[field]
            if data != None:
                new_vals[field] = data
        
        if new_vals:
            found.update(new_vals)
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
        
def getAll():
    return Product.query.all()

