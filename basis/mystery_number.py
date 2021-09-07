import random

nb_try = 5

min_interval = 0
max_interval = 100

mystery_number = random.randint(min_interval, max_interval)
answer = ""
win = False


while not (nb_try == 0 or win):
    answer = input(
        f"Trouvez le nombre mystère !\nEntrez une valeur entre {min_interval} et {max_interval} : ")

    if (not answer.isdigit()) or (int(answer) > max_interval):
        print(
            f"Veuillez entrer une valeur entre {min_interval} et {max_interval}")
    elif int(answer) < mystery_number:
        nb_try -= 1
        print(f"Plus grand ! \nIl vous reste {nb_try} essai(s)")
    elif int(answer) > mystery_number:
        nb_try -= 1
        print(f"Plus petit ! \nIl vous reste {nb_try} essai(s)")
    elif int(answer) == mystery_number:
        win = True

    print("-" * 50)

print(f"Félicitation le nombre à trouver était {mystery_number}") if win and nb_try > 0 else print(
    f"Dommage ! Le nombre mystère était {mystery_number}")
