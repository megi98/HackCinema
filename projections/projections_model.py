class ProjectionModel:
	def __init__(self, *, projection_id, movie_id, projection_type, date, time):
		self.projection_id = projection_id
		self.movie_id = movie_id
		self.projection_type = projection_type
		self.date = date
		self.time = time