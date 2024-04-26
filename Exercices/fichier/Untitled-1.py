import json
import os

# Chemin du fichier JSON
chemin_fichier = "Exercices\fichier\music.json"

def charger_chansons():
    """
    Charge les informations sur les chansons depuis le fichier JSON.
    Si le fichier n'existe pas, retourne une liste vide.
    """
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r') as f:
            chansons = json.load(f)
        return chansons
    else:
        return []

def sauvegarder_chansons(chansons):
    """
    Sauvegarde les informations sur les chansons dans le fichier JSON.
    """
    with open(chemin_fichier, 'w') as fichier:
        json.dump(chansons, fichier, indent=4)

def ajouter_chanson(titre, artiste, categorie, score, chansons):
    """
    Ajoute une nouvelle chanson à la liste des chansons.

    Args:
        titre (str): Le titre de la chanson.
        artiste (str): L'artiste de la chanson.
        categorie (str): La catégorie de la chanson.
        score (int): Le score de la chanson sur 5.
        chansons (list): La liste actuelle des chansons.
    """
    nouvelle_chanson = {
        "titre": titre,
        "artiste": artiste,
        "categorie": categorie,
        "score": score
    }
    chansons.append(nouvelle_chanson)
    sauvegarder_chansons(chansons)
    print("La chanson a été ajoutée avec succès.")

def afficher_chansons(chansons):
    """
    Affiche les informations sur toutes les chansons.

    Args:
        chansons (list): La liste des chansons à afficher.
    """
    if not chansons:
        print("Aucune chanson n'est disponible.")
    else:
        print("Liste des chansons :")
        for index, chanson in enumerate(chansons, start=1):
            print(f"{index}. {chanson['titre']} - {chanson['artiste']} [{chanson['categorie']}] - Score: {chanson['score']}")

def main():
    # Chargement des chansons depuis le fichier JSON
    chansons = charger_chansons()

    while True:
        print("\nMenu :")
        print("1. Ajouter une nouvelle chanson")
        print("2. Afficher la liste des chansons")
        print("3. Quitter")

        choix = input("Entrez votre choix (1/2/3) : ")

        if choix == '1':
            titre = input("Titre de la chanson : ")
            artiste = input("Artiste de la chanson : ")
            categorie = input("Catégorie de la chanson : ")
            score = int(input("Score de la chanson sur 5 : "))
            ajouter_chanson(titre, artiste, categorie, score, chansons)
        elif choix == '2':
            afficher_chansons(chansons)
        elif choix == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez saisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()