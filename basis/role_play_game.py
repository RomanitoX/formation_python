from random import randint
import random

choice = ""
pass_turn = False

self_hp = 50
ennemy_hp = 50
nb_potions = 3
potion_rand_range = (15, 50)
self_damage_range = (5, 10)
ennemy_damage_range = (5, 15)

while not (self_hp < 0 or ennemy_hp < 0):

    if not pass_turn:
        choice = input(
            f"Souhaitez-vous attaquer (1) {'ou utiliser une potion (2) ?' if nb_potions > 1 else ''}")

        if not choice.isdigit() or (int(choice) > 2 and nb_potions > 0):
            print("Veuillez entrer une valeur correcte !")

        elif choice == "1":
            damage_dealt = randint(self_damage_range[0], self_damage_range[1])
            ennemy_hp -= damage_dealt
            print(
                f"Vous avez infligé {damage_dealt} points de dégats à l'ennemi")

        elif choice == "2":
            if nb_potions > 0:
                heal_value = randint(
                    potion_rand_range[0], potion_rand_range[1])
                nb_potions -= 1
                self_hp += heal_value
                pass_turn = True
                print(
                    f"Vous récupérez {heal_value} points de vie ({nb_potions} {' potions restantes' if nb_potions > 1 else ' potion restante'})")
            else:
                print("Vous n'avez plus de potions !")
    else:
        pass_turn = False
        print("Vous passez votre tour...")

    damage_received = randint(ennemy_damage_range[0], ennemy_damage_range[1])
    self_hp -= damage_received

    print(f"L'ennemi vous a infligé {damage_received} points de dégats")

    if self_hp > 0:
        print(f"Il vous reste {self_hp} points de vie.")
    else:
        print("Vous avez péri...")

    if ennemy_hp > 0:
        print(f"Il reste {ennemy_hp} points de vie à l'ennemi.")
    else:
        print("Bravo, vous avez vaincu ce vilain méchant !")

    print('-' * 50)
