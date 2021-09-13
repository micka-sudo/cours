import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    
    with open(DATA_FILE, "r") as fichier:
        movies_title = json.load(fichier)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    #creation methode pour lire et ecire film
    def _get_movies(self):
        with open(DATA_FILE, "r") as fichier:
            return json.load(fichier)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as fichier:
            json.dump(movies, fichier, indent=4)
    #  methode ajout de film
    def add_to_movies(self):
        # Recuperer la liste des films
        movies = self._get_movies()
        # Vérifier que n'est pas deja dans la lsite
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        #  Si ce n'est pas le cas on l'ajoute
        else:
            logging.warning(f"Le Film {self.title} est déja dans la liste")
            return False
        #  Si c'est le cas, on affiche un message avec le module logging
    #  methode pour enlever les films
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            

    


if __name__ == "__main__":
    movies = get_movies()
    print(movies)
   