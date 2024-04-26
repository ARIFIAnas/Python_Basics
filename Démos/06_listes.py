#on initialise une liste avec les corchets []
#Liste vide
ma_liste = [1,4,5,3,2] 

ma_liste2 = [1, 2, 3,"test" , True, ["a" , True , 25]]

print(ma_liste2)

# Afficher un élément de la liste (elle commence à l'index 0)

print(ma_liste2[0])
print(ma_liste2[3])

#Afficher un élément de la liste contenue dans la première : 
print(ma_liste2[5])
print(ma_liste2[5][1])

#modifier un element a un index précis
ma_liste2[0] = 80
print(ma_liste2) 

#pour trier une liste on utilise .sort()
ma_liste.sort()
print(ma_liste)
ma_liste.sort(reverse=True)
print(ma_liste)
#pour ajouter a la fin de la liste
ma_liste.append(30)
print(ma_liste)
#pour ajouter a un index précis : 
ma_liste.insert(2 , 10)
print(ma_liste)
# pour ajouter une liste a la suite d'une autre
ma_liste2.extend(ma_liste)
print(ma_liste2)
# /!\ si on utilise append , on ajoutera le 2eme liste dnas la 1er liste 
ma_liste2.append(ma_liste)
print(ma_liste2)
#vérifier le type de la variable
print(type(ma_liste2))
print(isinstance(ma_liste2 , list))
#pour retirer un élément via son index : 
ma_liste2.pop(0)
print(ma_liste2)

#pour retirer un element avec son contenu : 
ma_liste2.remove('test')
print(ma_liste2)

for element in ma_liste2 : 
    print(element)