import csv 

path = "Démos/10_csv/test.csv"

with open(path, mode='r') as fichier:
    reader = csv.reader(fichier,delimiter=";")
    print(reader)
    next(reader)
    for row in reader:
        print(row)
        for element in row :
            print(element)

with open(path, mode='a' , encoding='UTF-8' , newline="") as fichier:
    writer = csv.writer(fichier , delimiter=';')
    writer.writerow(["Titi" , "20" , "Paris"]) 
