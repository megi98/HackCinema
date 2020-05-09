from ..db import Database
from movie_model import MovieModel


class MovieGateway:
	def __init__(self):
		self.model = MovieModel(movie_id=None, name=None, rating=None)
		self.db = Database()


	def set_movie(self, movie_id, name, rating):
		self.model.movie_id = movie_id
		self.model.name = name
		self.model.rating = rating


	def add_movie(self, *, name, rating):
		query = f'''
		INSERT INTO movies (name, rating)
		  VALUES('{name}', {rating});
		'''

		self.db.cursor.execute(query)
		self.db.connection.commit()


	def get_movie_by_id(self, *, movie_id):
		query = f'''
		SELECT name, rating FROM movies
		  WHERE id = {movie_id};
		'''
		self.db.cursor.execute(query)

		movie = self.db.cursor.fetchone()
		self.db.connection.commit()

		return movie 


	def get_all_movies(self):
		query = '''
		SELECT * FROM movies
		  ORDER BY rating DESC;
		'''
		self.db.cursor.execute(query)

		movies = self.db.cursor.fetchall()
		self.db.connection.commit()

		return movies


	def get_all_projections(self):
		projections = self.db.show_all_projections()
		return projections
