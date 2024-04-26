def sauvegarder_secret(fichier, secret):
    """
    Sauvegarde le secret dans un fichier.

    Args:
        fichier (str): Le nom du fichier.
        secret (str): Le texte secret à sauvegarder.
    """
    with open(fichier, 'w') as f:
        f.write(secret)


def charger_secret(fichier):
    """
    Charge le secret depuis un fichier.

    Args:
        fichier (str): Le nom du fichier.

    Returns:
        str: Le secret chargé depuis le fichier, ou None si le fichier n'existe pas.
    """
    try:
        with open(fichier, 'r') as f:
            secret = f.read()
            return secret
    except FileNotFoundError:
        return None
    
def main():
    nom_fichier = "secret.txt"

    # Chargement du secret s'il existe, sinon initialisation à une chaîne vide
    secret = charger_secret(nom_fichier)
    if secret is None:
        print("Aucun secret trouvé. Veuillez en saisir un nouveau :")
        secret = input("Nouveau secret : ")

    while True:
        print("\nMenu :")
        print("1. Voir le secret")
        print("2. Modifier le secret")
        print("3. Quitter")

        choix = input("Entrez votre choix (1/2/3) : ")

        if choix == '1':
            if secret:
                print("Le secret est :", secret)
            else:
                print("Aucun secret n'est défini.")
        elif choix == '2':
            nouveau_secret = input("Entrez le nouveau secret : ")
            secret = nouveau_secret
            print("Le secret a été modifié avec succès.")
        elif choix == '3':
            sauvegarder_secret(nom_fichier, secret)
            print("Le secret a été sauvegardé. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez saisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()