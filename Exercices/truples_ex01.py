def operations_numeriques(nombre1, nombre2):
    somme = nombre1 + nombre2
    difference = nombre1 - nombre2
    if nombre2 != 0:
        quotient = nombre1 / nombre2
    else:
        quotient = "Division par zéro impossible"
    produit = nombre1 * nombre2
    return somme, difference, quotient, produit

def afficher_resultats(resultats):
    print("Somme :", resultats[0])
    print("Différence :", resultats[1])
    print("Quotient :", resultats[2])
    print("Produit :", resultats[3])

# Programme principal
print("Calcul de la somme, de la différence, du quotient et du produit de deux nombres.")

nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

resultats = operations_numeriques(nombre1, nombre2)
afficher_resultats(resultats)

