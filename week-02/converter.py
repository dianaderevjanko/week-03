#konstances
KM_TO_MILES = 0.621371
KG_TO_LBS = 2.20462
L_TO_GALLONS = 0.264172
USD_TO_EUR = 0.85235

# 1. Ieliekam visu bezgalīgā ciklā
while True:
    print('\n--- Konversijas kalkulators ---')   # Simbolu virkne \n--- un --- tavā kodā kalpo tikai un vienīgi vizuālajam noformējumam terminālī, lai tekstu būtu vieglāk lasīt
    izvele = input("Izvēlies (1-4) konvērsiju: 1)km<->mi, 2)kg<->lb 3)L<->gal 4)USD<->EUR  vai raksti 'exit', lai izietu: ")
    if izvele.lower() == 'exit':  # Ja lietotājs raksta 'exit' (neatkarīgi no lielajiem vai mazajiem burtiem), pārtraucam ciklu
        print("Paldies, ka izmantojāt konversijas kalkulatoru! Uz redzēšanos!")
        break
    #izvele = input("Izvelies konvērsiju: 1)km<->mi, 2)kg<->lb 3)L<->gal 4)USD<->EUR   ")
#pārbaudam lai izvēle būtu pareiza
    if izvele == "1":
        print('Izvelies virzienu: 1) KM/MI 2 )MI/KM ' )
        virziens = input("Ievadi virzienu: ")
        if virziens == "1" or virziens == "2":
            ievade = input("Ievadi vērtību, kuru vēlies konvertēt: ")
            vertiba = float(ievade.replace(',', '.'))
            if virziens == "1":
                rezultats = vertiba * KM_TO_MILES
                print(f"Rezultāts: {vertiba :.2f} km ir {rezultats:.2f} mi.")  #:.2f - noapaļo rezultātu līdz 2 cipariem aiz komata
            elif virziens == "2":
                rezultats = vertiba / KM_TO_MILES
                print(f"Rezultāts: {vertiba :.2f} mi ir {rezultats:.2f} km.")
        else:
            print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")

    elif izvele == "2":
        print('Izvelies virzienu: 1) KG/LB 2 )LB/KG ' )
        virziens = input("Ievadi virzienu: ")
        if virziens == "1" or virziens == "2":
            ievade = input("Ievadi vērtību, kuru vēlies konvertēt: ")
            vertiba = float(ievade.replace(',', '.'))
            if virziens == "1":
                rezultats = vertiba * KG_TO_LBS
                print(f"Rezultāts: {vertiba :.2f} kg ir {rezultats:.2f} lb.")  #:.2f - noapaļo rezultātu līdz 2 cipariem aiz komata
            elif virziens == "2":
                rezultats = vertiba / KG_TO_LBS
                print(f"Rezultāts: {vertiba :.2f} lb ir {rezultats:.2f} kg.")
        else:
            print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")
    
    elif izvele == "3":
        print('Izvelies virzienu: 1) L/GAL 2 )GAL/L ' )
        virziens = input("Ievadi virzienu: ")
        if virziens == "1" or virziens == "2":
            # Pajautājam vērtību un uzreiz salabojam iespējamo komata kļūdu
            ievade = input("Ievadi vērtību, kuru vēlies konvertēt: ")
            vertiba = float(ievade.replace(',', '.'))
    
            if virziens == "1":
                rezultats = vertiba * L_TO_GALLONS
                print(f"Rezultāts: {vertiba :.2f} L ir {rezultats:.2f} gal.")  #:.2f - noapaļo rezultātu līdz 2 cipariem aiz komata
            elif virziens == "2":
                rezultats = vertiba / L_TO_GALLONS
                print(f"Rezultāts: {vertiba :.2f} gal ir {rezultats:.2f} L.")
        else:
            print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")

    elif izvele == "4":
        print('Izvelies virzienu: 1) USD/EUR 2 )EUR/USD ' )
        virziens = input("Ievadi virzienu: ")
        if virziens == "1" or virziens == "2":
            # Pajautājam vērtību un uzreiz salabojam iespējamo komata kļūdu
            ievade = input("Ievadi vērtību, kuru vēlies konvertēt: ")
            vertiba = float(ievade.replace(',', '.'))
    
            if virziens == "1":
                rezultats = vertiba * USD_TO_EUR
                print(f"Rezultāts: {vertiba :.2f} USD ir {rezultats:.2f} EUR.")  #:.2f - noapaļo rezultātu līdz 2 cipariem aiz komata
            elif virziens == "2":
                rezultats = vertiba / USD_TO_EUR
                print(f"Rezultāts: {vertiba :.2f} EUR ir {rezultats:.2f} USD.")
            else:
                print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")
        else:
            print("Kļūda! Lūdzu, izvēlies pareizo virzienu.")

    else:
        print("Kļūda! Lūdzu, izvēlies pareizo kategoriju.")