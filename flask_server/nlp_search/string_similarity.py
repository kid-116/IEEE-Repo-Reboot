from thefuzz import fuzz

def sortProducts(prods, query):
    filteredProds = []
    for prod in prods:
        score = fuzz.token_set_ratio(prod.name, query)
        if score > 35:
            filteredProds.append(
                {"product": prod, "score": score})
    print(filteredProds)
    if filteredProds:
        filteredProds.sort(key=lambda prod: prod['score'], reverse=True)
        sortedProds = [prod['product'] for prod in filteredProds]
        print(sortedProds)
        return sortedProds
    else:
        return []
