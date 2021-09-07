import json

chemin = r"D:\Documents\Python\test.json"

with open(chemin, "r") as f:
    data = json.load(f)

data.append(5)

with open(chemin, "w") as f:
    json.dump(data, f, indent=4)
