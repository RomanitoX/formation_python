"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

from pathlib import Path

extensions = {
    # Musiques
    ".mp3": "Musiques",
    ".wav": "Musiques",
    ".flac": "Musiques",
    # Videos
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    # Images
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    # Documents
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

actual_dir = Path(__file__).parent.absolute()
actual_file = Path(__file__).name

files = [f for f in actual_dir.iterdir() if f.is_file()]

for f in files:
    if f.name != actual_file:
        output_dir = actual_dir / extensions.get(f.suffix.lower(), "Divers")
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir / f.name)
