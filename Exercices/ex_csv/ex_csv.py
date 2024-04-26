import csv 

path = "Exercices/ex_csv/ex_csv.csv"

def ajouter_info():
    titre = input("ajaouter un titre pour le produit : ")
    prix = input("ajouter un prix pour le produit : ")
    stock = input("ajouter le stock du produit : ")
    with open(path, mode='a' , encoding='UTF-8' , newline="") as fichier:
        writer = csv.writer(fichier , delimiter=';')
        writer.writerow([titre , prix , stock])

ajouter_info()

