from reservations_controller import ReservationController


class ReservationView:
	def __init__(self):
		self.controller = ReservationController()


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


	def make_reservation(self, *, user_id, projection_id):
		print('Choose seat:')
		row = int(input('Row: '))
		col = int(input('Column: '))
		is_available = self.controller.check_if_seat_is_available(projection_id=projection_id, row=row, col=col)

		while is_available is False:
			print('This seat is already taken!')
			print('Choose seat:')
			row = int(input('Row: '))
			col = int(input('Column: '))
			is_available = self.controller.check_if_seat_is_available(projection_id=projection_id, row=row, col=col)

		reservation = self.controller.make_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)
		while type(reservation) is str:
			print(reservation)
			row = int(input('Row: '))
			col = int(input('Column: '))
			reservation = self.controller.make_reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)

		print("Congratulations! You've just made your new reservation")

