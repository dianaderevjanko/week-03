#Pirmā funkcija is_email(text) E-pastam jābūt tekstam, jāsatur @ un pēc tam vismaz viens punkts ..
def is_email(text):
    """
    Pārbauda, vai teksts atbilst vienkāršam e-pasta formātam.
    
    Parametri: text (str)
    Atgriež: bool (True, ja satur @ un punktu pēc tā)
    """
    if not isinstance(text, str):
        return False
    
    if "@" not in text:
        return False
        
    parts = text.split("@")
    # Pārbaudām vai pēc @ ir teksts un tajā ir punkts
    if len(parts) == 2 and "." in parts[1] and len(parts[1]) > 1:
        return True
        
    return False

#Otrā funkcija is_phone_number(text) Šeit mums jāpārbauda vai teksts sākas ar +371 un vai pēc tam seko tieši 8 cipari.
def is_phone_number(text):
    """
    Pārbauda, vai teksts ir LV telefona numurs (+371 XXXXXXXX).
    """
    if not isinstance(text, str):
        return False
        
    # Pārbaudām sākumu
    if not text.startswith("+371 "):
        return False
        
    # Noņemam sākumu un pārbaudām atlikumu
    numura_dala = text.replace("+371 ", "")
    
    # Vai palikuši tieši 8 simboli un tie visi ir cipari?
    return len(numura_dala) == 8 and numura_dala.isdigit()  

#3. funkcija: is_valid_age(age) Šeit mums jāpārbauda divas lietas: vai tas ir skaitlis un vai tas ir loģiskās robežās (no 0 līdz 150 gadiem).
def is_valid_age(age):
    """
    Pārbauda, vai vecums ir vesels skaitlis diapazonā 0-150.
    """
    # Pārbaudām, vai tips ir int (vesels skaitlis)
    if not isinstance(age, int):
        return False
    
    # Pārbaudām robežas
    return 0 <= age <= 150

# 4. funkcija: is_strong_password(text) Šeit mums jāpārbauda, vai parole ir vismaz 8 simbolus gara, satur lielo un mazo burtu, ciparu un speciālo simbolu.
def is_strong_password(text):
    """
    Pārbauda, vai parole ir stipra: vismaz 8 simboli, satur burtus un ciparus.
    """
    if not isinstance(text, str) or len(text) < 8:
        return False
    
    # Pārbaudām, vai ir vismaz viens burts UN vismaz viens cipars
    has_alpha = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    
    return has_alpha and has_digit  

# 5. is_valid_date(text)        # YYYY-MM-DD formāts (pamata pārbaude) 

def is_valid_date(text):
    """
    Pārbauda, vai teksts atbilst datuma formātam YYYY-MM-DD.
    """
    if not isinstance(text, str):
        return False
    
    parts = text.split("-")
    
    if len(parts) != 3:
        return False
    
    year, month, day = parts
    
    # Pārbaudām, vai gads, mēnesis un diena ir cipari
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    
    # Pārbaudām gadu, mēnesi un dienu loģiskās robežas
    year = int(year)
    month = int(month)
    day = int(day)
    
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    
    return True
   
if __name__ == "__main__":
    # Testējam is_email funkciju
    print("--- E-pasta pārbaude ---")
    print(f"Vai 'komposs@gmail.com' ir derīgs? {is_email('komposs@gmail.com')}")  # True
    print(f"Vai 'komposs.gmail.com' ir derīgs? {is_email('komposs.gmail.com')}")  # False
    
    # Testējam is_valid_age funkciju
    print("\n--- Vecuma pārbaude ---")
    print(f"Vecums 25: {is_valid_age(25)}")   # True
    print(f"Vecums -5: {is_valid_age(-5)}")   # False
    print(f"Vecums 200: {is_valid_age(200)}")  # False

    # Testējam is_phone_number funkciju
    print(f"Numurs '+371 12345678': {is_phone_number('+371 12345678')}")  # True
    print(f"Numurs '+37112345678': {is_phone_number('+37112345678')}")   # False

    # Testējam is_strong_password funkciju
    print(f"Parole 'Parole123' ir stipra? {is_strong_password('Parole123')}")  # True
    print(f"Parole 'Parole' ir stipra? {is_strong_password('Parole')}")     # False
    print(f"Parole '12345678' ir stipra? {is_strong_password('12345678')}")   # False

    # Testējam is_valid_date funkciju
    print("\n--- Datuma pārbaude ---")
    print(f"Datums '2024-03-27': {is_valid_date('2024-03-27')}") # True
    print(f"Datums '2024-13-01': {is_valid_date('2024-13-01')}") # False (mēnesis 13)
    print(f"Datums 'abc-de-fg': {is_valid_date('abc-de-fg')}")   # False (nav cipari)