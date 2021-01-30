from peewee import *

db = SqliteDatabase('movies.db')

print('01 Movie modelo running...')

print('01.1 Creating Model...')


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    adult = BooleanField()
    backdrop_path = TextField()
    id = IntegerField()
    original_language = CharField()
    original_title = CharField()
    overview = TextField()
    popularity = DecimalField()
    poster_path = CharField()
    release_date = DateField()
    title = TextField()
    video = TextField()
    vote_average = DecimalField()
    vote_count = IntegerField()

print('01.2 End Movie modelo running...')
# print('Creating Table...')
# db.create_tables([Movie])

# data = movie_data.informacion()
# data_movie = data.get('results')
#
# for i in data_movie:
#     Movie.create(
#         adult=i.get('adult'),
#         backdrop_path=i.get('backdrop_path'),
#         id=i.get('id'),
#         original_language=i.get('original_language'),
#         original_title=i.get('original_title'),
#         overview=i.get('overview'),
#         popularity=i.get('popularity'),
#         poster_path=i.get('poster_path'),
#         release_date=i.get('release_date'),
#         title=i.get('title'),
#         video=i.get('video'),
#         vote_average=i.get('vote_average'),
#         vote_count=i.get('vote_count')
#     )
# print('Movie model listo')
