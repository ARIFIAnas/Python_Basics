# # nombre_max = None
# for i in range(6):
#     nombre = int(input("Entrez le nombre : "))


#     if nombre_max is None or  nombre > nombre_max:
#         nombre_max = nombre

# print(">>>>>" , nombre_max)

def vérification_adn(adn):
    """Vérifie si la chaîne d'ADN est valide"""
    lettres_valides = {'a', 't', 'c', 'g'}
    return all(lettre in lettres_valides for lettre in adn)

def saisie_adn():
    """Récupère une saisie utilisateur et vérifie sa validité"""
    adn = input("Veuillez saisir une chaîne d'ADN : ").lower() 
    while not vérification_adn(adn):
        print("La chaîne d'ADN saisie n'est pas valide. Elle doit contenir uniquement les lettres 'a', 't', 'c' et 'g'.")
        adn = input("Veuillez saisir une nouvelle chaîne d'ADN : ").lower()
    return adn

def proportion(adn, sequence):
    """Retourne le nombre d'occurrences de la séquence dans la chaîne d'ADN"""
    return adn.count(sequence)


chaine_adn = saisie_adn()
sequence_adn = input("Veuillez saisir une séquence d'ADN à rechercher : ").lower()
while not vérification_adn(sequence_adn):
    print("La séquence d'ADN saisie n'est pas valide. Elle doit contenir uniquement les lettres 'a', 't', 'c' et 'g'.")
    sequence_adn = input("Veuillez saisir une nouvelle séquence d'ADN : ").lower()

nb_occurrences = proportion(chaine_adn, sequence_adn)
print(f"Le nombre d'occurrences de la séquence '{sequence_adn}' dans la chaîne d'ADN est : {nb_occurrences}")