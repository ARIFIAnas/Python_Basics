from Exercices.eXERCICES.adn import *

chaine_adn = saisie_adn("Veuillez saisir votre chaine d'ADN : ")
sequence = saisie_adn("Veuillez saisir la séquence d'ADN : ")

print('Chaine :', chaine_adn)
print('Séquence :', sequence)

occurence = occurrence_sequence(chaine_adn, sequence)
pourcentage = pourcentage_sequence(chaine_adn, sequence, occurence)

print(f"il y a {pourcentage}% de {sequence} dans la chaine {chaine_adn}")