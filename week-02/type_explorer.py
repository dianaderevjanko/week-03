vards = input("Kā tevi sauc?") 
print("Sveiki, " + str(vards) + "!") #str() - pārvērš jebko par tekstu
while True: 
    # Sākam bezgalīgu ciklu
    gads = input ('kāds tavs dzimšanas gads? ')
    if gads.isdigit(): # Pārbaudām, vai ievadītais teksts sastāv tikai no cipariem Ja tie ir cipari, pārtraucam ciklu ar 'break'
        break
    # Ja ir burti vai tukšums, rādām kļūdu un cikls sākas no jauna
    else:
        print('Kļūda! Lūdzu, ievadiet gadu, izmantojot tikai ciparus.')
print('Tavs dzimšanas gads ir ' + str(gads) + '.') # Kad cikls ir beidzies, izdrukājam rezultātu
rezultāts = 2026 - int(gads) # int() - pārvērš tekstu vai daļskaitli par veselu skaitli
print ('Tātad tev ir ' + str(rezultāts) + ' gadi.')