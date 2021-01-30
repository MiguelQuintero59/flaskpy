from flask import render_template, Blueprint
from movie_data import agregar_informacion

load = Blueprint('load', __name__)

print('03. Movie load running')
@load.route('/load')
def load_movies():
    message = agregar_informacion()
    return render_template('load.html', datos=message)
