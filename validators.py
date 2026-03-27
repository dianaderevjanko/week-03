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
   
if __name__ == "__main__":
    # Testējam is_email funkciju
    print(is_email("komposs@gmail.com"))  # True
    print(is_email("komposs.gmail.com"))  # False
    
    # Testējam is_phone_number funkciju
    print(is_phone_number("+371 12345678"))  # True
    print(is_phone_number("+37112345678"))   # False