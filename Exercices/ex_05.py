# n = int(input("veuillez saisir un nombre enter : "))

# if n % 3 == 0 :
    # print("Le nombre es divisible par 3")
# else: 
    # print("Le nombre n'est pas divisible par 3")

nbr_photocopie = int (input("entrer le nombre de photocopies : "))

if nbr_photocopie < 10 :
    print("Le prix est : " , nbr_photocopie * 0.5)

elif 10 <= nbr_photocopie <= 20:
    print("le prix est : ", nbr_photocopie * 0.4)
else : 
    print("le prix est : " , nbr_photocopie * 0.3)

age_bebe = int(input("entrer l'age de votre bebe : "))

if 3<= age_bebe >= 6 :
    print("Baby")
elif 7<= age_bebe >= 8:
    print("Poussin")
elif 9<= age_bebe >= 10:
    print("Pupille")
elif 11<= age_bebe >= 12:
    print("Minime")
else:
    print("Cadet")
