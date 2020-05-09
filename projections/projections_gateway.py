from projections_model import ProjectionModel
from ..db import Database


class ProjectionGateway:
	def __init__(self):
		self.model = ProjectionModel(projection_id=None, movie_id=None, projection_type=None, date=None, time=None)
		self.db = Database()


	def set_projection(self, projection_id, movie_id, projection_type, date, time):
		self.model.projection_id = projection_id
		self.model.movie_id = movie_id
		self.model.projection_type = projection_type
		self.model.date = date
		self.model.time = time


	def add_projection(self, *, movie_id, projection_type, date, time):
		query = f'''
		INSERT INTO projections (movie_id, type, date, time)
		  VALUES({movie_id}, '{projection_type}', '{date}', '{time}');
		'''

		self.db.cursor.execute(query)
		self.db.connection.commit()


	def get_projection_by_id(self, *, projection_id):
		query = f'''
		SELECT movie_id, type, date, time FROM projections
		  WHERE id = {projection_id};
		'''
		self.db.cursor.execute(query)

		projection = self.db.cursor.fetchone()
		self.db.connection.commit()

		return projection


	def get_projections_by_movie_id(self, *, movie_id):
		query = f'''
		SELECT * FROM projections
		  WHERE movie_id = {movie_id}
		  ORDER BY date;
		'''
		self.db.cursor.execute(query)

		projections = self.db.cursor.fetchall()
		self.db.connection.commit()

		return projections


	def get_projections_by_movie_id_and_date(self, *, movie_id, date):
		query = f'''
		SELECT * FROM projections
		  WHERE movie_id = {movie_id} AND date LIKE '{date}'
		  ORDER BY date;
		'''
		self.db.cursor.execute(query)

		projections = self.db.cursor.fetchall()
		self.db.connection.commit()

		return projections


	def get_all_projections(self):
		query = 'SELECT * FROM projections;'
		self.db.cursor.execute(query)

		projections = self.db.cursor.fetchall()
		self.db.connection.commit()

		return projections

