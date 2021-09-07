from pathlib import Path

p = Path("D:/Images")

print(p)

for f in p.iterdir():
    print(f.name)

liste = [f for f in p.iterdir() if f.is_dir()]

print(f"Folder content : {liste}")

images = [f for f in p.glob("*.jpg") if f.is_file()]

print(f"Images : {images}")

for f in p.glob("*.jpg"):
    print(f.name)
