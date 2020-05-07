from ..db import Database


class MovieGateway:
	def __init__(self):
		self.db = Database()


	def add_movie(self, *, name, rating):
		self.db.add_movie(name=name, rating=rating)


	def get_movie_by_id(self, id):
		movie = self.db.get_movie_by_id(movie_id=id)
		return movie[0]


	def show_all_movies(self):
		return self.db.show_movies()


	def add_projection(self, *, movie_id, type, date, time):
		self.db.add_projection(movie_id=movie_id, type=type, date=date, time=time)


	def get_projections_by_movie_id(self, movie_id):
		projections = self.db.show_projections_by_movie_id(movie_id)
		return projections


	def get_projections_by_movie_id_and_date(self, movie_id, date):
		projections = self.db.show_projections_by_movie_id_and_date(movie_id, date)
		return projections


	def get_all_projections(self):
		projections = self.db.show_all_projections()
		return projections
