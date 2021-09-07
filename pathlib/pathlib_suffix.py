from pathlib import Path

p = Path(__file__).parent.absolute()
p = p / "readme.txt"

print(p)

print(p.parent / p.stem)

p = p.parent / (p.stem + "-test" + p.suffix)
p.touch()