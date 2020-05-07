from model import UserModel
from ..db import Database



class UserGateway:
	def __init__(self):
		self.model = UserModel(id=None, email=None, password=None)
		self.db = Database()


	def create_user(self, *, email, password):
		self.model.validate(email, password)
		hashpass = self.model.hash_password(password)
		self.db.create_user(email=email, password=hashpass)


	def get_user_by_id(self, *, email):
		user = self.db.get_user_by_id(email=email)

		if user == 0:
			raise Exception("No user with this data. Please sign up.")
		else:
			return user


	def show_all_users(self):
		return self.db.show_all_users()



