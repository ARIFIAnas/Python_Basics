def panne_moteur(liste):
    liste.append(liste.pop(0))  # Mettre le premier élément à la fin de la liste

def passe_en_tete(liste):
    premier = liste.pop(0)  # Retirer le premier élément
    liste.insert(1, premier)  # Insérer le premier élément à la deuxième position

def sauve_honneur(liste):
    dernier = liste.pop()  # Retirer le dernier élément
    avant_dernier = liste.pop(-1)  # Retirer l'avant-dernier élément
    liste.append(dernier)  # Ajouter le dernier à la fin
    liste.insert(-1, avant_dernier)  # Insérer l'avant-dernier avant dernier

def tir_blaster(liste):
    liste.pop(0)  # Enlever le premier élément

def retour_inattendu(liste, concurrent):
    liste.append(concurrent)  # Ajouter le concurrent à la fin de la liste

# Exemple d'utilisation :
concurrents = ["ANAS", "JOHNNY", "SALAHUDDIN", "ASLI", "SORIBA"]

panne_moteur(concurrents)
print("Après la panne moteur :", concurrents)

passe_en_tete(concurrents)
print("Après le passage en tête :", concurrents)

sauve_honneur(concurrents)
print("Après le sauvetage de l'honneur :", concurrents)

tir_blaster(concurrents)
print("Après le tir de blaster :", concurrents)

retour_inattendu(concurrents, "JP")
print("Après le retour inattendu :", concurrents)