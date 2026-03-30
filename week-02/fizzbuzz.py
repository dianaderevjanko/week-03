import sys
# sys.argv ir saraksts ar visu, ko raksti terminālī.
# sys.argv[0] ir faila nosaukums (fizzbuzz.py)
# sys.argv[1] būs pirmais skaitlis, ko ierakstīsi aiz nosaukuma

if len(sys.argv) > 1:
    # Paņemam pirmo argumentu un pārvēršam par int
    n = int(sys.argv[1])
else:
    # Ja lietotājs aizmirsa ierakstīt skaitli, pajautājam to
    n = int(input("N netika norādīts. Ievadi ciklu skaitu N: "))

try:
    n = int(ievade) #Ja lietotājs ievadīs burtu, int() funkcija "salūzīs" un izmetīs ValueError. Tāpēc izmantojam try-except bloku, lai noķertu šo kļūdu un informētu lietotāju par nepareizu ievadi.

print(f"\n--- Python FIZZBUZZ līdz {n} ---")

for skaitlis in range(1, n + 1):  # uzsākst cikls no 1 līdz N (ieskaitot)
    # Pirmo pārbaudām kopīgo dalāmību (ar 3 UN 5)
    # Izmantojam modulo operatoru %, kas atgriež atlikumu (0 nozīmē, ka dalās)
    if skaitlis % 3 == 0 and skaitlis % 5 == 0:  # skaitlis dalās ar 3 un 5
        print("FizzBuzz")
    elif skaitlis % 3 == 0:  # Dalot skaitli ar 3, atlikums ir nulle." (Tātad skaitlis dalās ar 3).
        print("Fizz")
    elif skaitlis % 5 == 0:  # Dalot skaitli ar 5, atlikums ir nulle." (Tātad skaitlis dalās ar 5)
        print("Buzz")
    elif skaitlis % 7 == 0:  # Dalot skaitli ar 7, atlikums ir nulle." (Tātad skaitlis dalās ar 7)
        print("Jazz")
    else:
        print(skaitlis)

except ValueError:
    print("Kļūda! Lūdzu, ievadiet veselu skaitli, nevis burtus.")