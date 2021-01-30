# API TheMovieDB al database
import json
from urllib.request import urlopen
from models.movie_modelo import Movie, db
from peewee import IntegrityError
import models.movie_modelo

API_KEY = 'a3f67b0fc1e52a12440e53cb4a7d275f'

print('02 Movie data running...')

# URL de moviedb
url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-CO&page=1'
r = urlopen(url)


# datos en json
def informacion():
    return json.loads(r.read())
data = informacion()

print ("02.1 La data de la informacion es tipo " + str(type(data)))

data_movie = data.get('results')

print("02.2 Starting agregar funcion...")


def agregar_informacion():
    for i in data_movie:
        Movie.create(
            adult=i.get('adult'),
            backdrop_path=i.get('backdrop_path'),
            id=i.get('id'),
            original_language=i.get('original_language'),
            original_title=i.get('original_title'),
            overview=i.get('overview'),
            popularity=i.get('popularity'),
            poster_path=i.get('poster_path'),
            release_date=i.get('release_date'),
            title=i.get('title'),
            video=i.get('video'),
            vote_average=i.get('vote_average'),
            vote_count=i.get('vote_count')
        )

db.create_tables([Movie], safe=True)
var = agregar_informacion()
# print(var)

if __name__ == '__main__':
    informacion()

print("02.3 End Movie data")