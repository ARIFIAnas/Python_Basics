#print => Afficher une chaine de caractere dans la console
print("hello world")

#print sur plusieurs lignes
print("""
        ligne 1
            ligne 2
                ligne 3
    """)

#print multiple avec des espaces 
print(1,"test",1,9)

# Une variable
ma_variable = 8
print(ma_variable)

# si je veux commenter j'utilise #
# si je veux commenter plusieur ligne j'utilise "ctrl + :"
# si je veux dupliquer une ligne "alt + shift + haut et bas"
# si je veux deplacer une ligne "alt + haut ou bas"

# Les numériques 
var = 55 #int
print(type(var)) #verifier le type d'un varibale ( type())
var = 55.0 #float
print(type(var))

# le type chaine (str)
var ="exemple"
print(type(var))

# Les booléens
mon_bool = True
print(type(mon_bool))
mon_bool = False

test_maj = "test".upper()
print(test_maj)

# Récuperation 
mon_input = input("Veuillez saisir un nbr entier : ")
print(mon_input)

# Le cast (passer d'un type de variable a un autre)
mon_input_int = int(mon_input)
print(type(mon_input_int))

mon_input_2 = int(input("Veuillez saisir un autre nombre : "))
print(type(mon_input_2))

print("mon_input_2 = ", mon_input_2 , "mon_input_1 = ", mon_input)
print(f"mon_input_2 = {mon_input_2} mon_input_1 = {mon_input}")

# raw-string
print('te\nst')
print(r'te\nst')
