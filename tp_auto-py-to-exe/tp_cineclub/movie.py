import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    return [Movie(movie_title) for movie_title in movies_title]


class Movie():

    def __init__(self, title: str) -> None:
        self.title = title.title()

    def __str__(self) -> str:
        return self.title

    def add_to_movies(self) -> bool:
        movies = list(self._get_movies())

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré !")
            return False

    def remove_from_movies(self) -> bool:
        movies = list(self._get_movies())

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(
                f"Le film {self.title} n'existe pas dans la liste !")
            return False

    # private
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    # private
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)


if __name__ == "__main__":
    print(get_movies())
