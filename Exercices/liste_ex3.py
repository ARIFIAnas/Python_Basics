def saisie_notes():
    notes = []
    while True:
        note = float(input("Entrez une note (ou une note négative pour terminer) : "))
        if note < 0:
            break
        notes.append(note)
    return notes

def afficher_menu():
    print("\nMenu :")
    print("1. Afficher la note maximale")
    print("2. Afficher la note minimale")
    print("3. Afficher la moyenne")
    print("4. Quitter")

def note_maximale(notes):
    return max(notes)

def note_minimale(notes):
    return min(notes)

def moyenne(notes):
    return sum(notes) / len(notes)

# Programme principal
print("Bienvenue !")
notes = saisie_notes()

while True:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == '1':
        print("La note maximale est :", note_maximale(notes))
    elif choix == '2':
        print("La note minimale est :", note_minimale(notes))
    elif choix == '3':
        print("La moyenne est :", moyenne(notes))
    elif choix == '4':
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez entrer un nombre entre 1 et 4.")