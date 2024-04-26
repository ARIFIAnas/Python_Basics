from math import pi

r = int(input("veuillez saisir le rayon : "))
h = int(input("veuillez saisir la hauteur : "))

v = (pi * r * r * h)/3

print(f"le volume est = {v:^8.2f}")
