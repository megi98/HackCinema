from reservations_gateway import ReservationGateway


class ReservationController:
	def __init__(self):
		self.gateway = ReservationGateway()


	def make_reservation(self, *, user_id, projection_id, row, col):
		try:
			self.gateway.model.validate(row, col)
		except Exception as err:
			return str(err)

		self.gateway.make_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)
		return True


	def delete_reservation(self, *, user_id, projection_id, row, col):
		self.gateway.delete_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)


	def get_taken_seats_for_projection(self, *, projection_id):
		return self.gateway.get_taken_seats_for_projection(projection_id=projection_id)


	def available_seats_count(self, *, projection_id):
		available_seats_count = 100 - len(self.get_taken_seats_for_projection(projection_id=projection_id))
		return available_seats_count


	def check_if_seat_is_available(self, *,projection_id, row, col):
		seat = row, col
		taken_seats = self.get_taken_seats_for_projection(projection_id=projection_id)

		if seat in taken_seats:
			return False

		return True


	def get_all_reservations_for_user(self, *, user_id):
		return self.gateway.get_all_reservations_for_user(user_id=user_id)
