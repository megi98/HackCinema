from projections_gateway import ProjectionGateway


class ProjectionController:
	def __init__(self):
		self.gateway = ProjectionGateway()


	def add_projection(self, *, movie_id, projection_type, date, time):
		self.gateway.add_projection(movie_id=movie_id, projection_type=projection_type, date=date, time=time)


	def get_projection_by_id(self, *, projection_id):
		projection = self.gateway.get_projection_by_id(projection_id=projection_id)

		if projection is None:
			return False

		self.gateway.set_projection(projection_id, projection[0], projection[1], projection[2], projection[3])
		return projection


	def get_projections_by_movie_id(self, *, movie_id):
		return self.gateway.get_projections_by_movie_id(movie_id=movie_id)


	def get_projections_by_movie_id_and_date(self, *, movie_id, date):
		return self.gateway.get_projections_by_movie_id_and_date(movie_id=movie_id, date=date)


	def get_all_projections(self):
		return self.gateway.get_all_projections()
