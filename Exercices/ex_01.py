a = 1 
b = 2 

a = b
b = a - 1
print("a =" ,a)
print ("b = ", b)

# La bonne méthode bonne pratique 
a=1
b=2
# variable pour sauvegarder la valeur de a 
c=a
# tmp = a  -> variable temporaire
a=b
b=c
print("a =" ,a)
print ("b = ", b)

