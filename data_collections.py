skaitli = [1, 2, 3, 4, 5, 8, 10, 12]   #veidojam mainīgo skaitli, kurā ir saraksts ar 5 elementiem 
print(skaitli)  #lai redzētu rezultātu terminālī.

#Metode .append() vienmēr pievieno jaunu elementu saraksta pašās beigās.
skaitli.append(15)
print(skaitli)

#Metode .pop() izdara divas lietas: tā izņem pēdējo elementu no saraksta un to "atdod" (tu vari to saglabāt citā mainīgajā vai vienkārši izdzēst).
skaitli.pop()   #izsauc .pop() savam sarakstam un izprintē sarakstu pēdējo reizi. Redzēsi, ka pēdējais skaitlis ir pazudis.
print(skaitli)

#Summas aprēķināšana ar for ciklu
summa = 0   #izveidojam mainīgo summa, kurā glabāsim rezultātu. Sākumā tā ir 0, jo mēs vēl neesam saskaitījuši nevienu skaitli.
for skaitlis in skaitli:   #izveidojam for ciklu,
    summa += skaitlis # vai summa = summa + skaitlis
print("Summa:", summa)

#Lai aprēķinātu vidējo vērtību, tev ir jāizdara viena vienkārša darbība: kopējā summa jādala ar skaitļu skaitu.
summa = 0
skaits = 0
for skaitlis in skaitli:
    summa += skaitlis
    skaits += 1  # vai skaits = skaits + 1                                          
vidējā = summa / skaits if skaits > 0 else 0
print("Vidējā vērtība:", vidējā)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

#izveidot jaunu sarakstu tikai ar pāra skaitļiem (for + if)
para_skaitli = []   #tukšs saraksts, kurā glabāsim pāra skaitļus
for skaitlis in skaitli:        #Cikls ies cauri tavam oriģinālajam sarakstam, bet if pārbaudīs, vai skaitlis dalās ar 2 bez atlikuma (% 2 == 0).
    if skaitlis % 2 == 0:       #Ja skaitlis ir pāra, tas tiks pievienots jaunajam sarakstam ar .append() metodi.
        para_skaitli.append(skaitlis)
print("Pāra skaitļi:", para_skaitli)  #izprintē pāra skaitļu sarakstu pēc cikla beigām.

#Šķēlumi (slices) eizmaina oriģinālo sarakstu, bet izveido tā "kopiju" pēc taviem nosacījumiem.
pirmie_tris = skaitli[:3] #Mēs norādām, ka gribam sākt no sākuma un apstāties pie indeksa 3 (kurš pats netiek iekļauts).
pedejie_divi = skaitli[-2:] #skaitām no beigām, izmantojot mīnusa zīmi. -2 nozīmē "sākt divas pozīcijas no beigām".
katrs_otrais = skaitli[::2] #atstājam sākumu un beigas tukšas (tas nozīmē "visu sarakstu"), bet pieliekam soli 2, lai izdrukātu katru otro skaitli.
print(f"Pirmie trīs skaitļi: {pirmie_tris}, \nPēdējie divi skaitļi: {pedejie_divi}, \nKatrs otrais skaitlis: {katrs_otrais}") #\n (jaunas rindas simbols) tiek izmantots, lai izdrukātu katru rezultātu jaunā rindā.

#B daļa - vārdnīcas (dictionaries)
dati = {"Anna": 85, "Jānis": 72, "Līga": 95}
print (dati)
dati["Māris"] = 88  #pievieno jaunu ierakstu vārdnīcai

dati["Jānis"] = 78  #maina Jāņa vērtību uz 78

del dati["Līga"]  #izdzēš Līgas ierakstu no vārdnīcas

#for, lai skaisti izprintētu katru studentu un viņa balles.
for vards, balle in dati.items():
    print(f"Students {vards} ieguva {balle} balles.")