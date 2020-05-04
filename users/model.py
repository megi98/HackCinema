SPECIAL_SYMBOLS = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','"',"'",'<',',','>','.','?','/']

class UserModel:
	def __init__(self, *, id, email, username, password):
		self.id = id
		self.email = email
		self.username = username
		self.password = password

	@staticmethod
	def validate(email, password):
		if self.email.count('@') != 1:
			raise ValueError('Incorrect email.')

		inex_at = email.index('@')

		if self.email.count('.') != 1:
			raise ValueError('Incorrect email.')

		index_period = email.index('.')

		if index_at > index_period:
			raise ValueError('Incorrect email.')

		if len(self.password) < 8:
			raise ValueError('Invalid password.')

		count_special_symbols = 0
		for symbol in self.password:
			if symbol in SPECIAL_SYMBOLS:
				count_special_symbols += 1

		if count_special_symbols < 1:
			raise ValueError('Invalid password.')

		count_capital_letter = 0
		for symbol in self.password:
			if symbol.isupper():
				count_capital_letter += 1

		if count_capital_letter < 1:
			raise ValueError('Invalid password.')
				


