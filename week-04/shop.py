import sys
import storage 
import utils 

def add_item(name, qty):
    """Pievieno produktu, meklējot cenu datubāzē vai prasot lietotājam."""
    prices = storage.load_prices()
    qty = int(qty)

    if name in prices:
        old_price = prices[name]
        print(f"Atrasta cena produktam '{name}': {old_price:.2f} EUR/gab.")
        izvele = input("[A]kceptēt vai [M]ainīt cenu? ").upper()
        
        if izvele == "M":
            price = float(input(f"Ievadi jauno cenu priekš '{name}': "))
            storage.save_price(name, price)
        else:
            price = old_price
    else:
        print(f"Cena produktam '{name}' nav zināma.")
        price = float(input(f"Ievadi cenu priekš '{name}': "))
        storage.save_price(name, price)

    # Saglabājam iepirkumu sarakstā
    items = storage.load_list()
    new_item = {"name": name, "qty": qty, "price": price}
    items.append(new_item)
    storage.save_list(items)
    
    line_total = utils.calc_line_total(new_item)
    print(f"✓ Pievienots: {name} x {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

def list_items():
    items = storage.load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    
    print("\nIepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        line_total = utils.calc_line_total(item)
        print(f"  {i}. {item['name']} x {item['qty']} — {item['price']:.2f} EUR/gab. = {line_total:.2f} EUR")

def show_total():
    items = storage.load_list()
    total_price = utils.calc_grand_total(items)
    total_units = utils.count_units(items)
    print(f"Kopā: {total_price:.2f} EUR ({total_units} vienības, {len(items)} produkti)")

def clear_list():
    storage.save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    # 1. Pārbaudām, vai ir vismaz viena komanda
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add|list|total|clear]")
        return
       
    command = sys.argv[1].lower()

    # 2. Apstrādājam komandas
    if command == "add" and len(sys.argv) == 4:
        # Tagad add gaida tikai nosaukumu un daudzumu (kopā 4 argumenti)
        add_item(sys.argv[2], sys.argv[3])
    elif command == "list":
        list_items()
    elif command == "total":
        show_total()
    elif command == "clear":
        clear_list()
    else:
        print("Nepareiza komanda vai nepareizs argumentu skaits!")

if __name__ == "__main__":
    main()