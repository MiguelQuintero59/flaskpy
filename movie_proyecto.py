from flask import Flask

from models.movie_modelo import Movie, db
from views.movie_home import home
from views.movie_detail import profile
from views.movie_load import load

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(load)


def main():
    print('04. Creating Table ...')
    db.create_tables([Movie], safe=True)
    app.run()


if __name__ == '__main__':
    main()
