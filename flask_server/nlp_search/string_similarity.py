from thefuzz import fuzz
from dotenv import load_dotenv
import os

load_dotenv()

def sortProducts(prods, query):
    filteredProds = []
    for prod in prods:
        score = fuzz.token_set_ratio(prod.name, query)
        if score > int(os.getenv('SIMILARITY_CUTOFF')):
            filteredProds.append(
                {"product": prod, "score": score})
    if filteredProds:
        filteredProds.sort(key=lambda prod: prod['score'], reverse=True)
        sortedProds = [prod['product'] for prod in filteredProds]
        # print(sortedProds)
        return sortedProds
    else:
        return []
