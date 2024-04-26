# 1- Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide

def verification_adn(chaine):
    for lettre in chaine:
        if lettre not in 'actg':
            # resultat = False
            # break
            return False
    return True

# 2- Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
# chaîne d’ADN valide sous forme de chaîne

def saisie_adn(question):
    ma_chaine = input(question)

    while not verification_adn(ma_chaine):
        print("Erreur de saisie !")
        ma_chaine = input(question)
    
    return ma_chaine

# Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
# séquence d’ADN Elle renverra le d’occurrences de la séquence dans la chaîne

def occurrence_sequence(chaine, sequence):
    return chaine.count(sequence)

def pourcentage_sequence(chaine, sequence, occurence):
    return round(occurence * len(sequence) * 100 / len(chaine), 2)
