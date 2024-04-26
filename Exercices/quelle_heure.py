#def quelle_heure(heure="12h00"):
    #print("il est", heure)

#quelle_heure()  
#quelle_heure("14h00")  

def compter_lettre_a(chaine):
    count_a = 0
    for lettre in chaine:
        if lettre == "a":
            count_a += 1
    return count_a

# Exemples d'utilisation :
print(compter_lettre_a("abaaaba"))  # Affichera 2
print(compter_lettre_a("mixer"))  # Affichera 0

#def compter_lettre_a(chaine):
#    return chaine.count("a")

# Exemples d'utilisation :
#print(compter_lettre_a("abba"))  # Affichera 2
#print(compter_lettre_a("mixer"))  # Affichera 0    