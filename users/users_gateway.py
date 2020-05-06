from model import UserModel
from ..db import Database


class UserGateway:
	def __init__(self):
		self.model = UserModel()
		self.db = Database()


	def create_user(self, *, email, password):
		self.model.validate(email, password)
		hashpass = self.model.hash_password(password)
		self.db.create_user(email=email, password=hashpass)

		
	def get_movies(self):
		return self.db.show_movies()


	def show_seats_for_projection(self, *, projection_id):
		return self.db.get_seats(projection_id=projection_id)


	def make_reservation(self, *, projection_id, row, col):
		self.db.make_reservation(user_id=self.model.id, projection_id=projection_id, row=row, col=col)


	def all(self):
		pass


