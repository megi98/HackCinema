from users_gateway import UserGateway


class UserController:
	def __init__(self):
		self.users_gateway = UserGateway()


	def create_user(self, email, password):
		self.users_gateway.create_user(email=email, password=password)


	def get_user_by_id(self, email):
		try:
			user = self.users_gateway.get_user_by_id(email=email)
		except Exception as exc:
			return str(exc)

		return user
