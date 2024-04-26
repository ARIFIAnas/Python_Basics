# mon_dict = {"k1": 'valeur un', "k2": 25443, "k3": 3.14, "k4": {1: 'blabla'}}
# print(mon_dict)
# print(mon_dict['k3']) # 3.14
# print(mon_dict['k4'][1]) # blabla
# print(mon_dict.values()) # ['valeur un', 25443, 3.14, {&: "blabla"}]
# print(mon_dict.keys()) # ["k1", "k2", "k3", "k4"]
# print(mon_dict.items()) # {"k1": 'valeur un', "k2": 25443, "k3": 3.14, "k4": {1: 'blabla'}}
# for key, value in mon_dict.items():
#  print(f"key : {key}, value : {value}") # key : k1, value : valeur un ect...

 # pour créer un dictionnaire
mon_dict = {}
 
mon_dict = {
    "Clé 1" : "Valeur 1",
    2 : 1,
    True : False
}
 
# JSON -> JavaScript Object Notation
personne = {
    "Prénom" : "Christophe",
    "Nom" : "Ringot",
    "Age" : None
}
 
# Pour accéder à la valeur liée à la clé d'un dictionnaire : 
print(f"Mon prénom : {personne['Prénom']}")
 
# Ici, on re-affecte la valeur de la clé :
personne["Prénom"] = "Toto"
 
print(f"Mon prénom : {personne['Prénom']}")
 
# Pour ajouter un élément dans mon dictionnaire :
personne["Téléphone"] = "0101010101"
 
print(personne)
 
# Pour supprimer une entrée du dictionnaire :
# Attention : Exception si la clé n'éxiste pas !
del personne["Age"]
 
# Même chose :
# personne.pop("Age")
 
# Supprime et renvoie l'élément (tuple) :
# personne.popitem("Age")
 
for cle, valeur in personne.items():
    print(f"ma clé : {cle}, valeur : {valeur}")
 
# Pour fusionner deux dictionnaires ensemble :
personne.update(mon_dict)
print(personne)
 
toto = {
    "Prénom" : "Toto",
    "Nom" : "Tata",
    "Age" : 18
}
 
tata = {
    "Prénom" : "Tata",
    "Nom" : "Toto",
    "Age" : 18
}
 
titi = {
    "Prénom" : "Titi",
    "Nom" : "Toto",
    "Age" : 18
}
 
annuaire = [toto, tata, titi]
 
print(annuaire)
 
for personne in annuaire:
    print("Personne n°", annuaire.index(personne)+1)
    for cle, valeur in personne.items():
        print(cle, valeur)