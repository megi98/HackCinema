from users_gateway import UserGateway


class UserController:
	def __init__(self):
		self.gateway = UserGateway()


	def signup(self, *, email, password):
		try:
			self.gateway.model.validate(email, password)
			hashpass = self.gateway.model.hash_password(password)
			self.gateway.create_user(email=email, password=hashpass)
		except Exception as err:
			return str(err)


	def login(self, *, email, password):
		return self.gateway.set_user(email=email, password=password)


	def get_users_id(self):
		return self.gateway.get_users_id()


	def get_all_users(self):
		return self.gateway.get_all_users()
