from app import db

SHORT_TITLE = 17

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

    def getShortName(self):
        if len(self.name) < SHORT_TITLE:
            return self.name
        else:
            return self.name[:SHORT_TITLE] + '...'

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
            print(f"Product {pid} updated successfully")
        else:
            print("Invalid field(s)")
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
        
def getAll():
    return Product.query.all()

def getByCategory(cat):
    found = Product.query.filter_by(category= cat)
    if found:
        print(f"Products found in {cat}")
    else:
        print(f"No products found in {cat}")
    return found

def getCategories():
    found = Product.query.all()
    if found:
        return [prod.category for prod in found]
    else:
        print("No products found")
    return None


    
