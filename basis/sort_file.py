from pathlib import Path

dirs = {
    # Images
    ".ai": "Images",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".ico": "Images",
    ".ps": "Images",
    ".psd": "Images",
    ".svg": "Images",
    ".tif": "Images",
    ".tiff": "Images",
    # Vidéos
    ".mp4": "Vidéos",
    ".avi": "Vidéos",
    ".mkv": "Vidéos",
    ".mov": "Vidéos",
    ".webm": "Vidéos",
    ".3g2": "Vidéos",
    ".3gp": "Vidéos",
    ".flv": "Vidéos",
    ".h264": "Vidéos",
    ".m4v": "Vidéos",
    ".mpg": "Vidéos",
    ".mpeg": "Vidéos",
    # Archives
    ".zip": "Archives",
    "tar.gz": "Archives",
    ".7z": "Archives",
    ".rar": "Archives",
    ".rpm": "Archives",
    ".deb": "Archives",
    ".arj": "Archives",
    ".z": "Archives",
    # Documents
    ".pdf": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".tex": "Documents",
    ".wpd": "Documents",
    # Audio
    ".aif": "Musique",
    ".cda": "Musique",
    ".mid": "Musique",
    ".midi": "Musique",
    ".mp3": "Musique",
    ".mpa": "Musique",
    ".ogg": "Musique",
    ".wav": "Musique",
    ".wma": "Musique",
    ".wpl": "Musique",
    # ISO et médias
    ".bin": "ISOs",
    ".dmg": "ISOs",
    ".iso": "ISOs",
    ".toast": "ISOs",
    ".vcd": "ISOs",
    # Base de données
    ".dat": "Base de données",
    ".db": "Base de données",
    ".dbf": "Base de données",
    ".log": "Base de données",
    ".mdb": "Base de données",
    ".sav": "Base de données",
    ".sql": "Base de données",
    ".tar": "Base de données",
    ".xml": "Base de données",
    # Executable
    ".apk": "Executable",
    ".bat": "Executable",
    ".bin": "Executable",
    ".cgi": "Executable",
    ".pl": "Executable",
    ".com": "Executable",
    ".exe": "Executable",
    ".gadget": "Executable",
    ".jar": "Executable",
    ".msi": "Executable",
    ".py": "Executable",
    ".wsf": "Executable",

}

sorted = False

sorted_dir = Path(__file__).parent.absolute()
actual_file = Path(__file__).name

while not sorted:
    choice = input(
        "Trier les fichiers dans le dossier courant (1) ou spécifier le dossier ? (2)")

    if (not int(choice.isdigit())) or (int(choice.isdigit()) and int(choice) > 2):
        print("Veuillez écrire une valeur valide !")

    elif choice == "1":
        sorted_dir = Path(__file__).parent.absolute()

    elif choice == "2":
        specified_path = input(
            "Veuillez spécifier le chemin du dossier à trier : ")

        sorted_dir = Path(specified_path)

    if choice == "1" or choice == "2":
        files = [f for f in sorted_dir.iterdir() if f.is_file()]

        for f in files:
            if not f.name == actual_file:
                output_dir = sorted_dir / dirs.get(f.suffix.lower(), "Autres")
                output_dir.mkdir(exist_ok=True)
                f.rename(output_dir / f.name)

        sorted = True
