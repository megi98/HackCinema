from ..db import Database


class ReservationGateway:
	def __init__(self):
		self.db = Database()


	def make_reservation(self, *, user_id, projection_id, row, col):
		self.db.make_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)


	def delete_reservation(self, *, user_id, projection_id, row, col):
		self.db.del_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)


	def get_taken_seats_for_projection(self, *, projection_id):
		taken_seats = self.db.get_seats(projection_id=projection_id)
		return taken_seats


