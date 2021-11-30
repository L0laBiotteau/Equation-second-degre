from math import sqrt

def equation_second_degre (a,b,c):
    delta= b**2-4*a*c
    if delta <0:
        texte = " L'équation n'a pas de solution"
    elif delta == 0.0:
        texte = "Il y a une seule solution"
        solution = -b/(2*a)
    elif delta > 0:
        texte = " L'équation a deux solutions"
        solution_1 = (-b + sqrt (delta)) / (2*a)
        soltuion_2 = (-b - sqrt (delta)) / (2*a)
    return texte

print(str(equation_second_degre (8, 0, 4)))
