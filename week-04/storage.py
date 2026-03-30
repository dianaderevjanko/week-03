#Šis fails nodrošinās datu saglabāšanu.
import json
import os

# Fails tiks izveidots tajā pašā mapē, kurā atrodas šis skripts
FILENAME = "shopping.json"

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