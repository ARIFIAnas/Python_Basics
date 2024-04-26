def voir_adresse(adresses):
    for _ in adresses : 
        print("L'adresse est : " , adresses)

def ajouter_adresse(adresses):

    adresse ={}
    adresse["Numéro de voie"] = input("Numéro de voie : ")
    adresse["Complément"] = input("Complément : ")
    adresse["Intitulé de voie"] = input("Intitulé de voie : ")
    adresse["Commune"] = input("Commune : ")
    adresse["Code postal"] = input("Code postal : ")
    adresses.append(adresse)

def editer_adresse(adresses):
    print("list of adresses : " , adresses)
    for _ in range(len(adresses)) : 
        adresses[_] = ajouter_adresse()
    
def supprimer_adresse(adresses ,adresse):
    print("list of adresses : " , adresses)
    adresses[adresse].pop()

# Programme principal
print("Gestion des adresses")

adresses = []

while True:
    print("\nMenu :")
    print("1. Ajouter une adresse")
    print("2. Éditer une adresse")
    print("3. Supprimer une adresse")
    print("4. Visualiser les adresses")
    print("5. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == '1':
        ajouter_adresse(adresses)
    elif choix == '2':
        editer_adresse(adresses)
    elif choix == '3':
        supprimer_adresse(adresses)
    elif choix == '4':
        voir_adresse(adresses)
    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")


