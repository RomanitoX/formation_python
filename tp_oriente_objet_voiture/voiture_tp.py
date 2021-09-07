class Voiture:
    essence = 100

    def afficher_reservoir(self):
        print(f"Laa voiture contient {self.essence} litres d'essence")
    
    def roule(self, km):
        if self.essence == 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return
        elif self.essence <= 10:
            print("Vous n'avez bientôt plus d'essence !")
        else:
            print("lezgonguueeeee !!!")

        self.essence = self.essence - (km * 5) / 100

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")

choice = ""

while not exit:
    print("Bienvenu sur la route !")
    choice = input()
