path = input('Veuillez entre le chemin du fichier : ')

try:
    with open(path, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Fichier introuvable")
except UnicodeDecodeError:
    print("Fichier illisible")
finally:
    print("Fin du script")