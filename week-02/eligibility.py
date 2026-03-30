# 1. ievades dati
vecums = int(input("Ievadiet savu vecumu: "))
autoaplieciba = input("Vai jums ir autovadītāja apliecība? (yes/no): ").lower()
veterans = input("Vai esat veterāns? (yes/no): ").lower()
students = input("Vai esat students? (yes/no): ").lower()
print("\n--- ------------- ---")

# 2. Kompleksais loģiskais nosacījums
if (vecums >= 21 and autoaplieciba == "yes"):
    print("Auto īre:    Jā! ")
elif (vecums < 21):
    print("Auto īre:    Nē! (pārāk jauns)")
elif autoaplieciba != "yes":
    print("Auto īre:    Nē! (nav apliecības)")

if (vecums >= 18):
    print("Balsot:      Jā! ")
else:    print("Balsot:      Nē!")

if not vecums >= 65 and not veterans == "yes":
    print("Saņemt senioru atlaidi: Nē! ")
else:    print("Saņemt senioru atlaidi: Jā!")

if (students == "yes" and 16 <= vecums <= 26):
    print("Saņemt studentu atlaidi:    Jā! ")
else:    print("Saņemt studentu atlaidi:    Nē!")

# 3. Veicam visas pārbaudes un saglabājam rezultātus mainīgajos
ire_atbilst = "Jā" if (vecums >= 21 and autoaplieciba == "yes") else "Nē"
balss_atbilst = "Jā" if (vecums >= 18) else "Nē"
senior_atbilst = "Jā" if (vecums >= 65 or veterans == "yes") else "Nē"
student_atbilst = "Jā" if (students == "yes" and 16 <= vecums <= 26) else "Nē"

# 4. Izdrukājam visu vienā f-stringā, izmantojot \n jaunām rindām
print(f"""
--- Kopsavilkums par personu ---
Vecums: {vecums}
Auto īre: {ire_atbilst}
Balsot: {balss_atbilst}
Senioru atlaide: {senior_atbilst}
Studentu atlaide: {student_atbilst}
--------------------------------
""")