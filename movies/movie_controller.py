from movies_gateway import MovieGateway


class MovieController:
	def __init__(self):
		self.movies_gateway = MovieGateway()


	def add_movie(self, name, rating):
		self.movies_gateway.add_movie(name=name, rating=rating)


	def get_movie_by_id(self, id):
		return self.movies_gateway.get_movie_by_id(id)


	def show_all_movies(self):
		return self.movies_gateway.show_all_movies()


	def add_projection(self, movie_id, type, date, time):
		self.movies_gateway.add_projection(movie_id=movie_id, type=type, date=date, time=time)


	def get_projections_by_movie_id(self, movie_id):
		return self.movies_gateway.get_projections_by_movie_id(movie_id)


	def get_projections_by_movie_id_and_date(self, movie_id, date):
		return self.movies_gateway.get_projections_by_movie_id_and_date(movie_id, date)


	def get_all_projections(self):
		return self.movies_gateway.get_all_projections()
