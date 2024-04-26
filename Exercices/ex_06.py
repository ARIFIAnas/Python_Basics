temperature = float(input("Entrez la température de l'eau : "))

if temperature < 0:
        print("SOLIDE")
elif temperature <= 100:
        print ("LIQUIDE")
else:
        print ("GAZEUX")
