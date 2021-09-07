from pathlib import Path

p = Path(__file__).parent.absolute()

print(p)

p = p / "readme.txt"

p.touch()

p.write_text("Bonjour")

print(p.read_text())
