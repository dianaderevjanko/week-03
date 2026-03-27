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

def countwords(text):   #3.funkcija
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

def clamp(num, low, high):  #4.funkcija
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

def is_prime(num):  #5.funkcija Šī funkcija pārbaudīs, vai skaitlis dalās tikai ar 1 un sevi.
    """
    Pārbauda, vai skaitlis ir pirmskaitlis.
    Parametri: num (int)
    Atgriež: bool (True ja ir, False ja nav)
    """
    if not isinstance(num, int):
        raise ValueError("Jāievada vesels skaitlis!")
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):   #6.funkcija Reizinājums no 1 līdz n (piem., 5! = 120).
    """Aprēķina n faktoriālu."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Jāievada ne-negatīvs vesels skaitlis!")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def total(numbers): #7.funkcija Sarakstu funkcija, kas saskaita visus skaitļus sarakstā.
    """Saskaita visus skaitļus sarakstā."""
    if not isinstance(numbers, list):
        raise ValueError("Jāievada saraksts!")
    s = 0
    for n in numbers:
        s += n
    return s

def average(numbers):   #8.funkcija Aprēķina vidējo vērtību no skaitļu saraksta.
    """Aprēķina vidējo vērtību."""
    if not numbers: return 0
    return total(numbers) / len(numbers)

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
    
    # 5. Is prime tests (Pirmskaitļi)
    print(f"Vai 7 ir pirmskaitlis? {is_prime(7)}")    # Jābūt True
    print(f"Vai 10 ir pirmskaitlis? {is_prime(10)}")  # Jābūt False

    # 6. Factorial tests (Faktoriāls)
    print(f"5! (faktoriāls): {factorial(5)}")         # Jābūt 120 (1*2*3*4*5)
    print(f"0! (faktoriāls): {factorial(0)}")         # Jābūt 1

    # 7. Total tests (Summa)
    testa_saraksts = [10, 20, 30, 40]
    print(f"Saraksta {testa_saraksts} summa: {total(testa_saraksts)}") # Jābūt 100

    # 8. Average tests (Vidējais)
    print(f"Saraksta {testa_saraksts} vidējais: {average(testa_saraksts)}") # Jābūt 25.0