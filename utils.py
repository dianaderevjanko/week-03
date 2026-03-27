def capitalize(text):  #1.funkcija
    """
    Pārveido teksta pirmo burtu par lielo.
    Parametri: text (str)
    Atgriež: str (tekstu ar lielo sākumburtu)
    Piemērs: capitalize("hello") -> "Hello"
    """
    # 1. Pārbaude (validācija) - vai mums iedots teksts?
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam!")
    
    # 2. Darbība - paņem pirmo burtu lielu un pieliec pārējo tekstu
    if len(text) == 0:
        return ""
    
    return text[0].upper() + text[1:]

def truncate(text, max_len=20): #2.funkcija
    """
    Apgriež tekstu, ja tas pārsniedz noteiktu garumu, un pieliek '...'.
    
    Parametri:
    text (str): Teksts
    max_len (int): Maksimālais burtu skaits (noklusējums ir 20)
    
    Atgriež: str
    Piemērs: truncate("Sveika, pasaule!", 5) -> "Sveik..."
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam!")

    if len(text) > max_len:
        return text[:max_len] + "..."
    
    return text

def countwords(text):
    """
    Saskaita vārdus tekstā, izmantojot tukšumzīmes kā sadalītāju.
    
    Parametri:
    text (str): Teksts
    
    Atgriež: int (vārdu skaits)
    Piemērs: countwords("Sveika pasaule") -> 2
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam!")
    
    # Sadalām tekstu vārdos, izmantojot atstarpes kā atdalītājus
    words = text.split()    # Izveido sarakstu ar vārdiem
    return len(words)   # Atgriež saraksta elementu skaitu

def clamp(num, low, high):
    """
    Ierobežo skaitli noteiktā diapazonā.
    
    Parametri:
    num (int, float): Skaitlis, kuru pārbaudīt.
    low (int, float): Minimālā robeža.
    high (int, float): Maksimālā robeža.
    
    Atgriež:
    int, float: Skaitlis robežās starp low un high.
    """
    # Pārbaudām, vai tiešām iedoti skaitļi
    if not all(isinstance(x, (int, float)) for x in [num, low, high]):
        raise ValueError("Visiem parametriem jābūt skaitļiem!")

    if num < low:
        return low
    if num > high:
        return high
    return num

#bloks pasaka: "Izpildi šos printus TIKAI tad, ja es palaižu tieši šo failu, bet ne tad, ja kāds to importē." koda testēšanai vai demonstrēšanai.   
if __name__ == "__main__":          
    # Šeit mēs izsaucam funkciju un printējam tās atbildi
    rezultats = capitalize("diana") #pirmais burts būs lielais, pārējie mazie
    print(f"Rezultāts: {rezultats}")

    print(truncate("Šis teikums ir ļoti garš", 10)) # Izdrukās: Šis teikum...
    print(truncate("Īss teksts"))                  # Izmantos 20, izdrukās visu tekstu, jo tas ir īsāks par 20.
    # Count words tests
    print(f"Vārdu skaits: {countwords('Šis ir tests ar pieciem vārdiem')}") 
    # Clamp tests
    print(f"Clamp (80 diapazonā 0-100): {clamp(80, 0, 100)}")   # Jāpaliek 80
    print(f"Clamp (150 diapazonā 0-100): {clamp(150, 0, 100)}") # Jākļūst par 100
    print(f"Clamp (-10 diapazonā 0-100): {clamp(-10, 0, 100)}") # Jākļūst par 0