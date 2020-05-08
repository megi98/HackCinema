from reservations_gateway import ReservationGateway


class ReservationController:
	def __init__(self):
		self.gateway = ReservationGateway()


	def make_reservation(self, *, user_id, projection_id, row, col):
		self.gateway.make_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)


	def delete_reservation(self, *, user_id, projection_id, row, col):
		self.gateway.delete_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)


	def get_taken_seats_for_projection(self, *, projection_id):
		return self.gateway.get_taken_seats_for_projection(projection_id=projection_id)


	def available_seats_count(self, *, projection_id):
		return self.gateway.available_seats_count(projection_id=projection_id)
		

	def check_if_seat_is_available(self, *, projection_id, row, col):
		return self.gateway.check_if_seat_is_available(projection_id=projection_id, row=row, col=col)


	def check_if_seat_is_out_of_range(self, *, row, col):
		return self.gateway.check_if_seat_is_out_of_range(row=row, col=col)
