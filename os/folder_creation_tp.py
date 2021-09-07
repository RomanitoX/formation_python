import os

chemin = "ENTREZ UN CHEMIN DE DOSSIER DANS LEQUEL CRÉER LA STRUCTURE"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

chemin = input(chemin)

for key, values in d.items():
    for val in values:
        os.makedirs(os.path.join(chemin, key, val))
