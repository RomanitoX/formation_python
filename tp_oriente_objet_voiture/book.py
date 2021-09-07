class Book:

    def __init__(self, nom, nombre_de_pages, prix) -> None:
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix


livre_HP = Book("Harry Potter", 300, 10.99)
livre_LOTR = Book("Le Seigneur des Anneaux", 400, 13.99)
