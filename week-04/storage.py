#Šis fails nodrošinās datu saglabāšanu.
import json
import os

# Fails tiks izveidots tajā pašā mapē, kurā atrodas šis skripts
FILENAME = "shopping.json"
PRICE_FILE = "prices.json"

def load_list():
    """Nolasa sarakstu no shopping.json. Ja faila nav, atgriež []."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """Saglabā sarakstu JSON formātā."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

# Šīs funkcijas nodrošinās cenu saglabāšanu un nolasīšanu, lai varētu atjaunināt cenas bez nepieciešamības mainīt kodu.
def load_prices():
    """Nolasa cenu vārdnīcu. Ja neeksistē, atgriež {}."""
    if not os.path.exists(PRICE_FILE):
        return {}
    with open(PRICE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_price(name, price):
    """Saglabā vai atjaunina cenu konkrētam produktam."""
    prices = load_prices()
    prices[name] = float(price)
    with open(PRICE_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)