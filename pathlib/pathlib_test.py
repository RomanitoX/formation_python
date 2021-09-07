from pathlib import Path

p = Path(__file__)

print(f"Nom : {p.name}")
print(f"Parent : {p.parent}")
print(f"Stem : {p.stem}")
print(f"Suffixe : {p.suffix}")
print(f"Suffixes : {p.suffixes}")
print(f"Parties : {p.parts}")
print(f"Il existe ? : {p.exists()}")
print(f"Est-ce un dossier ? : {p.is_dir()}")
print(f"Est-ce un fichier ? : {p.is_file()}")
