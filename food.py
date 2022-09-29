import requests
import json

BASE_URL = "https://fr.openfoodfacts.org/api/v2/produit/"
CODE_BARRE = input("Saisissez le code barre du produit : ")
SEARCH = f"{BASE_URL}{CODE_BARRE}.json"

response = requests.get(SEARCH)
data = json.loads(response.text)
listing = []

for i in data['product']:
    listing.append(i)
    print(data['product'][i], "\n")


#print(*listing, sep = "\n")
