increment = 0 
while increment < 10 :
    increment +=1
    if increment == 3 :
        continue # on passe a l'iteration suivante , les instructions ne sont pas executees
    elif increment == 5 :
        break # On arrete la boucle sans faire l'iteration suivante.
    print("boucle n°", increment)

#boucle infini
#while True : 
        #increment +=1
        #print(increment)
#while True : 
#        valeur = input("saisir STOP")
#        if valeur == 'STOP':
#              break
#       elif valeur == 'stop':
#             print("EN UPPERCASE")
#              continue
for i in range(0 , 10):
    print(i)
