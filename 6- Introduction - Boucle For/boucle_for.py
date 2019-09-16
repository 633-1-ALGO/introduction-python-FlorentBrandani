# Exemples de boucle for

print("Décomposition d'un mot en lettre")

chaine = "Hello World !"

for lettre in chaine:
    print("Lettre courante = ", lettre)
print("")

tableau = [30, 22, 35, 47, 15]

cpt = 0
for element in tableau:
    print("indice courant = ", cpt)
    print("element courant = ", element)
    print("-------------------")
    cpt = cpt + 1
print("")

print("Décompte du nombre d'execution de la boucle")
n = len(tableau)  # longueur du tableau
for i in range(0, n):  # "i" représentant l'indice courant et range une séquence de [0 à n-1]
    print("Execution n°:", i + 1, "Resultat : ", tableau[i])
