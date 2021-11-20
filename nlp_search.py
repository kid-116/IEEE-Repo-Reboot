from thefuzz import fuzz
from app import db
from models import getAll

def sortProducts(query):
    if query:
        prods = []
        for prod in getAll():
            prods.append({"product": prod, "score": fuzz.partial_ratio(prod.name, query)})
        prods.sort(key=lambda prod : prod['score'])
        return prods

print(sortProducts("hello world"))
