from controllers import UserController


class UserView:
	def __init__(self):
		self.controller = UserController()


	def welcome(self):
		print('Welcome in HackCinema! Please choose an option:')
		print('''
			[1] - to login
			[2] - to signup\n
			''')
		command = input('> ')

		while int(command) != 1 and int(command) != 2:
			print('Not existing option! Try again')
			command = input('> ')

		return command


	def signup(self):
		email = input('Email: ')
		password = input('Password: ')
		action = self.controller.signup(email=email, password=password)

		while type(action) is str:
			print(action, 'Please try again')
			email = input('Email: ')
			password = input('Password: ')
			action = self.controller.signup(email=email, password=password)

		print('''
			Thank you for your registration!
			You are logged in our system now :)\n
			''')


	def login(self):
		email = input('Email: ')
		password = input('Password: ')
		action = self.controller.login(email=email, password=password)

		while action is False:
			print('No user with this data. Please try again')
			email = input('Email: ')
			password = input('Password: ')
			action = self.controller.login(email=email, password=password)

		print('You are logged in our system now :)\n')


	def show_all_users(self):
		users = self.controller.get_all_users()
		for user in users:
			print(f'[{user[0]}] - {user[1]}')

