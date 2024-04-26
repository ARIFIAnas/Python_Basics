# def compter_lettre_a(chaine):
#     count_a = 0
#     count_b = 0
#     for lettre in chaine:
#         if lettre == "a" :
#             count_a += 1
#         elif lettre == "b" :
#             count_b += 1
#     return (count_a , count_b)

# print(compter_lettre_a("abaaaba"))
# print(compter_lettre_a("amixerb"))

def compter_lettre_a_count(chaine):
    return chaine.count('a') , chaine.count("b") , chaine.count("x")
    
print(compter_lettre_a_count("abaaaba"))
print(compter_lettre_a_count("amixerb"))
