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


	def available_seats_count(self, *, projection_id):
		available_seats_count = 100 - len(self.get_taken_seats_for_projection(projection_id=projection_id))
		return available_seats_count


	def check_if_seat_is_available(self, *,projection_id, row, col):
		seat = row, col
		taken_seats = self.get_taken_seats_for_projection(projection_id=projection_id)

		if seat in taken_seats:
			return False

		return True


	def check_if_seat_is_out_of_range(self, *, row, col):
		if row > 10 or col > 10:
			return False

		return True
