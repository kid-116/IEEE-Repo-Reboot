from thefuzz import fuzz
from models import getAll


def sortProducts(query):
    prods = []
    if query:
        for prod in getAll():
            prods.append(
                {"product": prod, "score": fuzz.partial_ratio(prod.name, query)})
        prods.sort(key=lambda prod: prod['score'])
    return prods
