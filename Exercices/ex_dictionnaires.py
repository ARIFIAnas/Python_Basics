def ajouter_adresse(adresses):
    adresse = {}
    print("Entrez les informations de l'adresse :")
    adresse["Numéro de voie"] = input("Numéro de voie : ")
    adresse["Complément"] = input("Complément : ")
    adresse["Intitulé de voie"] = input("Intitulé de voie : ")
    adresse["Commune"] = input("Commune : ")
    adresse["Code postal"] = input("Code postal : ")
    adresses.append(adresse)
    print("Adresse ajoutée avec succès.")

def editer_adresse(adresses):
    print("Liste des adresses :")
    for i, adresse in enumerate(adresses):
        print(i+1, "-", adresse)
    choix = int(input("Entrez le numéro de l'adresse à éditer : ")) - 1
    if choix >= 0 and choix < len(adresses):
        print("Entrez les nouvelles informations de l'adresse :")
        adresses[choix]["Numéro de voie"] = input("Nouveau numéro de voie : ")
        adresses[choix]["Complément"] = input("Nouveau complément : ")
        adresses[choix]["Intitulé de voie"] = input("Nouvel intitulé de voie : ")
        adresses[choix]["Commune"] = input("Nouvelle commune : ")
        adresses[choix]["Code postal"] = input("Nouveau code postal : ")
        print("Adresse éditée avec succès.")
    else:
        print("Adresse invalide.")

def supprimer_adresse(adresses):
    print("Liste des adresses :")
    for i, adresse in enumerate(adresses):
        print(i+1, "-", adresse)
    choix = int(input("Entrez le numéro de l'adresse à supprimer : ")) - 1
    if choix >= 0 and choix < len(adresses):
        del adresses[choix]
        print("Adresse supprimée avec succès.")
    else:
        print("Adresse invalide.")

def visualiser_adresses(adresses):
    print("Liste des adresses :")
    for i, adresse in enumerate(adresses):
        print(i+1, "-", adresse)

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
        visualiser_adresses(adresses)
    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
