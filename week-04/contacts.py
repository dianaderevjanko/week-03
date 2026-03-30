#1. solis: Pamata struktūra un ielāde/saglabāšana
import json
import sys
import os

CONTACTS_FILE = "contacts.json"

"""
os.path.exists: Pārbauda, vai fails vispār ir. Ja mēģināsi lasīt neesošu failu, programma "nobruks".
json.load: Pārvērš JSON tekstu atpakaļ par Python sarakstu/vārdnīcu.
json.dump: Pārvērš Python datus par JSON tekstu un ieraksta failā.
"""

def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu []."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

#2. solis: Kontakta pievienošanas funkcija

def add_contact(name, phone):
    # 1. Ielādē esošo sarakstu, izmantojot load_contacts()
    contacts = load_contacts()
    
    # 2. Izveido jaunu vārdnīcu: {"name": name, "phone": phone}
    new_entry = {"name": name, "phone": phone}
    # 3. Pievieno to sarakstam (atceries .append())
    contacts.append(new_entry)
    # 4. Saglabā atjaunoto sarakstu ar save_contacts(contacts)
    save_contacts(contacts)
    
    print(f"✓ Pievienots: {name} ({phone})")

#3. solis: Kontaktu izvadīšana, list - parādīt visus kontaktus

def list_contacts():
    """Ielādē un izprintē visus kontaktus no faila."""
    contacts = load_contacts()
    
    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return

    print("Kontakti:")
    for i, contact in enumerate(contacts, 1):
        # i ir kārtas numurs, contact ir vārdnīca
        print(f"  {i}. {contact['name']} — {contact['phone']}")

#4. solis: search (atrast konkrētu)

def search_contacts(query):
    """Meklē kontaktus pēc vārda daļas (query)."""
    contacts = load_contacts()
    
    # Izmantojam saraksta filtrēšanu, ko apguvām iepriekš
    found = [c for c in contacts if query.lower() in c['name'].lower()]
    
    if not found:
        print(f"Neviens kontakts ar vārdu '{query}' netika atrasts.")
        return

    print(f"Atrasti {len(found)} kontakti:")
    for i, contact in enumerate(found, 1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")

#5. solis: "Smadzenes" — main() un sys.argv (pēdējais solis, lai programma strādātu terminālī ar komandām add, list, search.)
'''
sys.argv ir saraksts, kurā Python glabā visu, ko tu ieraksti terminālī pēc python contacts.py.
sys.argv[0] ir faila nosaukums (contacts.py)
sys.argv[1] ir komanda (add, list vai search)

'''
def main():
    # Ja lietotājs nav ievadījis nevienu komandu
    if len(sys.argv) < 2:
        print("Lietošana: python contacts.py [add|list|search] [dati]")
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 4:
        add_contact(sys.argv[2], sys.argv[3])
    elif command == "list":
        list_contacts()
    elif command == "search" and len(sys.argv) == 3:
        search_contacts(sys.argv[2])
    else:
        print("Nepareiza komanda vai trūkst argumentu!")

if __name__ == "__main__":
    main()

