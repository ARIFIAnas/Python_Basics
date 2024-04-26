def recuperer_nombre(nombre) : 
    return nombre, nombre * 2 # tuple packing => on se sert d'un tuple retourner plusieurs valeurs

print(recuperer_nombre(2))
# principe d'unpacking : on 'découpe' notre tuple en plusieurs variables 
nombre, nombre_fois_2 = recuperer_nombre(15)
print(f"Mon nombre : {nombre} multiplier par deux : {nombre_fois_2}")

# La variable underscore "_" dans python sert à se débarasser des valuers inutiles.
_, nombre = recuperer_nombre(3)


