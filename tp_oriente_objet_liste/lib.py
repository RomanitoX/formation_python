from genericpath import exists
import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()


class Liste(list):

    def __init__(self, name) -> None:
        self.nom = name

    def ajouter(self, element) -> bool:
        if not isinstance(element, str):
            raise ValueError(
                "Vous ne pouvez ajouter que des chaînes de caractères.")

        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return False

    def enlever(self, element) -> bool:
        if element in self:
            self.remove(element)
            return True

        return False

    def afficher(self) -> None:
        print(f"Ma liste de {self.nom} :")
        for elem in self:
            print(f" - {elem}")

    def sauvegarder(self) -> bool:
        path = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(path, "w") as f:
            json.dump(self, f, indent=4)

        return True


if __name__ == "__main__":
    liste = Liste("test")
    liste.ajouter("pipoi")
    liste.ajouter("caca")
    liste.ajouter("popo")
    liste.ajouter("lol")
    liste.afficher()
    liste.sauvegarder()
