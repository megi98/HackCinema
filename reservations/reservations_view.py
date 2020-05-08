from reservations_controller import ReservationController
from reservation_model import ReservationModel


class ReservationView:
	def __init__(self):
		self.controller = ReservationController()
		self.model = ReservationModel(user_id=None, projection_id=None, row=None, col=None)
		self.num_tickets = None


	def show_available_seats_count(self, *, projection_id):
		available_seats_count = self.controller.available_seats_count(projection_id=projection_id)
		return f'{available_seats_count} spots available'


	def show_map_for_projection(self, *, projection_id):
		cinema = []
		taken_seats = self.controller.get_taken_seats_for_projection(projection_id=projection_id)

		for i in range(10):
			row = ''
			for j in range(10):
				row += '.'
			cinema.append(row)

		for seat in taken_seats:
			row = seat[0] - 1
			col = seat[1] - 1
			cinema[row] = list(cinema[row])
			cinema[row][col] = 'X'
			cinema[row] = ''.join(cinema[row])

		for row in cinema:
			print(row)

