from ..db import Database
from reservation_model import ReservationModel


class ReservationGateway:
	def __init__(self):
		self.model = ReservationModel(user_id=None, projection_id=None, row=None, col=None)
		self.db = Database()


	def make_reservation(self, *, user_id, projection_id, row, col):
		query = f'''
		INSERT INTO reservations (user_id, projection_id, row, col)
		  VALUES({user_id}, {projection_id}, {row}, {col});
		'''
		self.db.cursor.execute(query)
		self.db.connection.commit()

		self.model.user_id = user_id
		self.model.projection_id = projection_id
		self.model.row = row
		self.model.col = col


	def delete_reservation(self, *, user_id, projection_id, row, col):
		query = f'''
		DELETE FROM reservations
		  WHERE user_id = {user_id} AND projection_id = {projection_id} AND row = {row} AND col = {col};
		'''

		self.db.cursor.execute(query)
		self.db.connection.commit()


	def get_taken_seats_for_projection(self, *, projection_id):
		query = f'''
		SELECT row, col FROM reservations
		  WHERE projection_id = {projection_id};
		'''

		self.db.cursor.execute(query)
		seats = self.db.cursor.fetchall()
		self.db.connection.commit()

		return seats


	def get_all_reservations_for_user(self, *, user_id):
		query = f'''
		SELECT * FROM reservations
		  WHERE user_id = {user_id};
		'''

		self.db.cursor.execute(query)
		reservations = self.db.cursor.fetchall()
		self.db.connection.commit()

		return reservations
	
