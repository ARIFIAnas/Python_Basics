age = int(input("votre Age : "))
salaire = int(input("salaire : "))
nombre_exp = int(input("exp : "))

if age < 30:
    print("Le candidat est trop jeune pour le poste.")
elif salaire > 40000:
    print("Le salaire demandé est trop élevé pour le poste.")
elif nombre_exp < 5:
    print("Le candidat n'a pas assez d'expérience pour le poste.")
else:
    print("Le profil du candidat est valable pour la candidature.")
