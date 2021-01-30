from flask import render_template, Blueprint
from models.movie_modelo import Movie

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    movies = Movie.select()
    return render_template('index.html', datos=movies)


print('01.3 End Movie home...')