import random # Modulis nejauša skaitļa ģenerēšanai

# 1. Sagatavošanās
iedomatais = random.randint(1, 100)  #random.randint(1, 100):Šī funkcija izvēlas vienu nejaušu skaitli.
meginajumi = 0   #Tas ir skaitītājs. Spēles sākumā lietotājs vēl nav veicis nevienu gājienu, tāpēc mēs iestatām vērtību uz 0
maks_meginajumi = 10   # Šī ir konstante (robeža)

print("\n--- Skaitļu minēšanas spēle (1-100) ---")

# 2. bezgalīgais cikls
while True: 
    ievade = input(f"Mēģinājums {meginajumi + 1}/{maks_meginajumi}. Ievadi skaitli (vai 'stop'): ")
    
# Iespēja iziet no spēles jebkurā brīdī
    if ievade.lower() == 'stop':
        print("Spēle pārtraukta.")
        break
        
    try:
        minējums = int(ievade)
        meginajumi += 1 # Pieskaitām mēģinājumu tikai tad, ja tas ir skaitlis
        
        if minējums == iedomatais:
            print(f"UZVARA! Tu uzminēji ar {meginajumi}. reizi!")
            break # Pārtraucam ciklu, jo uzvarējām
        elif minējums < iedomatais:
            print("Par mazu!")
        else:
            print("Par lielu!")

         # Pārbaudām, vai mēģinājumi nav beigušies
        if meginajumi >= maks_meginajumi:
            print(f"Zaudējums! Beidzās mēģinājumi. Mans skaitlis bija {iedomatais}.")
            break # Pārtraucam ciklu, jo mēģinājumi beidzās
            
    except ValueError:
        print("Kļūda! Lūdzu, ievadi veselu skaitli.")
print("Paldies par spēli!")