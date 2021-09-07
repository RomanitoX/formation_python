class Voiture:
    def __init__(self, marque):
        self.marque = marque
    def afficher_marque(self):
        print(f"La voiture est une {self.marque}")
 
voiture_01 = Voiture("Lamborghini")
Voiture.afficher_marque(voiture_01)
voiture_01.afficher_marque()