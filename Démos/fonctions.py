def hello_world():
    print ("Hello world ! ")


hello_world()

def bonjout_qui(nom,prenom):
    print(f"Bonjour {nom}, {prenom}")

bonjout_qui('Arifi','Anas')

def bonjour_johnny(nom="Johnny"):
    print(f"Bonjour {nom}")

bonjour_johnny()
bonjour_johnny("Anas")

def nombre():
    a = 2
    return a 
a = nombre()
b = a + 1 
print(a)
print(b)