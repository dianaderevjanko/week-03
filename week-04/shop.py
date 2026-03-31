import sys
import storage 
import utils # Pārliecinies, ka šis fails ir tajā pašā mapē!

def add_item(name, qty, price):
    items = storage.load_list()
    # Izveidojam vārdnīcu ar visiem 3 laukiem
    new_item = {"name": name, "qty": int(qty), "price": float(price)}
    items.append(new_item)
    storage.save_list(items)
    
    # Izmantojam utils aprēķinam
    line_total = utils.calc_line_total(new_item)
    print(f"✓ Pievienots: {name} x {qty} ({price} EUR/gab.) = {line_total:.2f} EUR")
    
def list_items():
    items = storage.load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    
    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        # Izmantojam utils, lai parādītu rindiņas kopsummu
        line_total = utils.calc_line_total(item)
        print(f"  {i}. {item['name']} x {item['qty']} — {item['price']:.2f} EUR/gab. = {line_total:.2f} EUR")

def show_total():
    items = storage.load_list()
    # Izmantojam jaunās funkcijas no utils.py
    total_price = utils.calc_grand_total(items)
    total_units = utils.count_units(items)
    print(f"Kopā: {total_price:.2f} EUR ({total_units} vienības, {len(items)} produkti)")

def clear_list():
    storage.save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add|list|total|clear]")
        return
    
    command = sys.argv[1].lower()

    # ŠEIT BIJA KĻŪDA: Jāiedod visi trīs sys.argv!
    if command == "add" and len(sys.argv) == 5:
        add_item(sys.argv[2], sys.argv[3], sys.argv[4])
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