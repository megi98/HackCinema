from movies_gateway import MovieGateway


class MovieController:
	def __init__(self):
		self.gateway = MovieGateway()


	def add_movie(self, *, name, rating):
		self.gateway.add_movie(name=name, rating=rating)


	def get_movie_by_id(self, *, movie_id):
		movie = self.gateway.get_movie_by_id(movie_id=movie_id)

		if movie is None:
			return False

		self.gateway.set_movie(movie_id, movie[0], movie[1])
		return movie


	def get_all_movies(self):
		return self.gateway.get_all_movies()
