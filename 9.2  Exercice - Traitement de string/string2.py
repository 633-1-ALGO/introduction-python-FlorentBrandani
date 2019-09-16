# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

print(texte.count("exemple"))
new_Texte = texte.replace("est", "représente")
print(new_Texte)
print(new_Texte[::-1])
