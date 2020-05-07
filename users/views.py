from controllers import UserController


class UserViews:
	def __init__(self):
		self.controller = UserController()


	def welcome(self):
		print('Welcome in HackCinema! Please enter your data to login:')
		email = input('Email: ')
		password = input('Password: ')

		user = self.controller.get_user_by_id(email)

		if user == 'No user with this data. Please sign up.':
			print(user)
			print('Enter your data: ')
			email = input('Email: ')
			password = input('Password: ')
			self.controller.create_user(email, password)
			print('Thank you for your registration!')

		print('You are logged in our system now :)')
		return user
	
