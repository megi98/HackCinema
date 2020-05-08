from controllers import UserController


class UserViews:
	def __init__(self):
		self.controller = UserController()
		self.user_id = None


	def get_user_id(self):
		return self.user_id


	def enter_data(self):
		email = input('Email: ')
		password = input('Password: ')

		try:
			self.controller.create_user(email, password)
		except Exception as err:
			print(f'{str(err)} Try again!')
		finally:
			return self.controller.get_user_by_id(email)


	def welcome(self):
		print('Welcome in HackCinema! Please enter your data to login:')
		email = input('Email: ')
		password = input('Password: ')

		self.user_id = self.controller.get_user_by_id(email)

		if self.user_id == 'No user with this data. Please sign up.':
			print(self.user_id)
			print('Enter your data: ')
			self.user_id = self.enter_data()
			while type(self.user_id) is str:
				self.user_id = self.enter_data()
			print('Thank you for your registration!')

		print('You are logged in our system now :)')

