# galvenā programma, kas izmantos storage.py
import sys
import storage # Importējam tavu storage.py failu

def add_item(name, price):
    items = storage.load_list()
    items.append({"name": name, "price": float(price)})
    storage.save_list(items)
    print(f"✓ Pievienots: {name} ({price} EUR)")

def list_items():
    items = storage.load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    
    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item['name']} — {item['price']:.2f} EUR")

def show_total():
    """Aprēķina un izvada saraksta kopsummu."""
    items = storage.load_list()
    # sum() saskaita visas cenas no saraksta
    total_price = sum(item['price'] for item in items)
    print(f"Kopā: {total_price:.2f} EUR ({len(items)} produkti)")

def clear_list():
    """Pilnībā iztukšo iepirkumu sarakstu."""
    storage.save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add|list|total|clear]")
        return
    
    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 4:
        add_item(sys.argv[2], sys.argv[3])
    elif command == "list":
        list_items()
    
    elif command == "total":
        show_total()
    elif command == "clear":
        clear_list()

    else:
        print("Nepareiza komanda vai trūkst argumentu!")


if __name__ == "__main__":
    main()