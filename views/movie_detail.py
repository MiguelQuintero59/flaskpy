from flask import render_template, Blueprint
from models.movie_modelo import Movie

profile = Blueprint('profile', __name__)


@profile.route('/profile/<id>/')
def detail(id):
    id_movie = Movie.get(
        id=id
    )
    return render_template('detail.html', pelicula=id_movie)
