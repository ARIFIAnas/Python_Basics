def main_menu():
    if secret is None:
        print("Aucun secret trouvé. Veuillez en saisir un nouveau :")
        secret = input("Nouveau secret : ")
    while True:
        print("=== MENU ===")
        print("1. Voir le secret")
        print("2. Modifier le secret")
        print("3. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in '123':
            return choice
        else:
            print("Erreur, réessayez !\n")
    
        match choice:
            case "1":
                voir_secret()
            case "2":
                modifier_texte()
            case "3":
                return False, None

def sauvgarder_secret(secret):
    
    with open("w") as fichier : 
       fichier.write(secret)

def voir_secret(secret):
    with open(fichier, 'r') as fichier:
            secret = fichier.read()
            return secret
    
def modifier_texte(fichier, contenu_a_ajouter):

    with open(fichier, 'a') as fichier:
        fichier.write(contenu_a_ajouter)

main_menu() 

