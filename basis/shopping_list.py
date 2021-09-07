leave = False
menu = ["Ajouter à la liste", "Retirer de la liste",
        "Afficher la liste", "Vider la liste", "Quitter le programme"]
choice = 0
error_string = "'{0}' n'est pas un choix valide !"
shopping_list = []
typed_input = ""

while not leave:
    print("Bienvenue sur l'application liste de course !")
    for i in range(len(menu)):
        print(f" {i + 1}: " + menu[i])
    choice = input("Choisissez une action à réaliser : ")

    if choice == "1":
        typed_input = input("Que désirez-vous ajouter à la liste ? ")
        shopping_list.append(typed_input)
        print(f"{typed_input} à bien été ajouté à la liste.")

    elif choice == "2":
        typed_input = input("Que désirez-vous retirer de la liste ? ")
        if shopping_list.count(typed_input) != 0:
            shopping_list.remove(typed_input)
            print(f"{typed_input} à bien été retiré de la liste.")
        else:
            print("L'objet recherché n'existe pas")

    elif choice == "3":
        if(len(shopping_list) == 0):
            print("La liste est vide !")
        else:
            print("Voici ce que contient la liste :")
            for i, element in enumerate(shopping_list):
                print(f"{i} - {element}")

    elif choice == "4":
        shopping_list.clear()
        print("La liste a bien été vidée !")

    elif choice == "5":
        leave = True
    else:
        print(error_string.format(choice))

    print("-" * 50)