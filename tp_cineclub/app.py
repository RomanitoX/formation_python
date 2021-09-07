from movie import Movie
from movie import get_movies
from PySide2 import QtCore, QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ciné club")
        self._setup_ui()
        self.populate_movies()
        self.setup_connections()

    def _setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit("")
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(
            QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete = QtWidgets.QPushButton("Retirer le(s) film(s)")

        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_delete)

    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            self._add_listWidget(movie)

    def setup_connections(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_delete.clicked.connect(self.remove_movie)

    def add_movie(self) -> bool:
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        result = movie.add_to_movies()

        if not result:
            self.le_movieTitle.setText("")
            return False

        self._add_listWidget(movie)
        self.le_movieTitle.setText("")

        return True

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

    def _add_listWidget(self, movie: Movie):
        lw_item = QtWidgets.QListWidgetItem(movie.title)
        lw_item.setData(QtCore.Qt.UserRole, movie)
        self.lw_movies.addItem(lw_item)


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()
