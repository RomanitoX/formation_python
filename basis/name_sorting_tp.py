name_list = []

with open(r"D:\Documents\Python\prenoms.txt", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    name_list.extend(line.split())

sorted_list = [name.strip(",. ") for name in name_list]

with open(r"D:\Documents\Python\prenoms_sorted.txt", "w") as f:
    f.write("\n".join(sorted(sorted_list)))