class ReservationModel:
	def __init__(self, *, user_id, projection_id, row, col):
		self.user_id = user_id
		self.projection_id = projection_id
		self.row = row
		self.col = col

	@staticmethod
	def validate(row, col):
		if row > 10 or col > 10:
			raise Exception('Lol...NO!')
