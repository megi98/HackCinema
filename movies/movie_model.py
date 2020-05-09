class MovieModel:
	def __init__(self, *, movie_id, name, rating):
		self.movie_id = movie_id
		self.name = name
		self.rating = rating


	def get_movie_id(self):
		return self.movie_id


	def get_movie_title(self):
		return self.name
