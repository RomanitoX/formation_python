from pathlib import Path
import shutil

# On récupère le dossier dans lequel se trouve le script actuel
p = Path(__file__).parent.absolute()

# On concatène au dossier actuel
p = p / "test_folder_parent" / "test_folder_enfant"
print(p)
p.mkdir(exist_ok=True, parents=True)

# Ajout du nom du fichier au path
p = p / "readme.txt"

# Création du fichier
p.touch()

# Suppression du fichier
p.unlink()

# Retour au parent
p = p.parent

# Suppression du parent
p.rmdir()

p = p.parent
print(p)

#Suppression de tout l'arbre
shutil.rmtree(p)

p = p.parent
print(p)
