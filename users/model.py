import hashlib


SPECIAL_SYMBOLS = '`~!@#$%^&*()_-+=|:;"<>.?/'


class UserModel:
	def __init__(self, *, user_id, email, password):
		self.user_id = user_id
		self.email = email
		self.password = password

	@staticmethod
	def validate(email, password):
		if email.count('@') != 1:
			raise ValueError('Incorrect email.')

		index_at = email.index('@')

		if email.count('.') != 1:
			raise ValueError('Incorrect email.')

		index_period = email.index('.')

		if index_at > index_period:
			raise ValueError('Incorrect email.')

		if len(password) < 8:
			raise ValueError('Invalid password.')

		count_special_symbols = 0
		for symbol in password:
			if symbol in SPECIAL_SYMBOLS:
				count_special_symbols += 1

		if count_special_symbols < 1:
			raise ValueError('Invalid password.')

		count_capital_letter = 0
		for symbol in password:
			if symbol.isupper():
				count_capital_letter += 1

		if count_capital_letter < 1:
			raise ValueError('Invalid password.')


	@staticmethod
	def hash_password(password):
		return hashlib.sha512(password.encode()).hexdigest()
