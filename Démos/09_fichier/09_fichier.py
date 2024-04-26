import os

path = "Démos/09_fichier/test.txt"

# if not os.path.exists(path):
#     fichier = open(path,"w")
#     fichier.write("test")
#     fichier.close()
# else:
#     fichier = open(path , 'r')
#     contenu = fichier.read()
#     print(f'contenu du fichier : {contenu}')
#     fichier.close()

if not os.path.exists(path):
   with open(path,"w") as fichier : 
       fichier.write("teteteteteteetetetetetetetetetetetete")
else:
#    with open(path , "r") as fichier : 
#       contenu = fichier.read()
#       print(f'contenu du fichier : {contenu}')
    with open(path, "a" , encoding='UTF-8') as fichier : 
        fichier.write("\nj'ajoute du text à la fin du fichier !!!!!!!!")