from model import UserModel
from ..db import Database


class UserGateway:
	def __init__(self):
		self.model = UserModel(user_id=None, email=None, password=None)
		self.db = Database()


	def create_user(self, *, email, password):
		query = f'''
		INSERT INTO users (email, password)
		  VALUES('{email}', '{password}');
		'''

		self.db.cursor.execute(query)
		self.db.connection.commit()


	def set_user(self, *, email, password):
		query = f'''
		SELECT id, email, password FROM users
		  WHERE email = '{email}' AND password = '{password}';
		'''
		self.db.cursor.execute(query)

		user = self.db.cursor.fetchone()
		self.db.connection.commit()

		if user is None:
			return False
		else:
			self.model.user_id = user[0]
			self.model.email = user[1]
			self.model.password = user[2]
			return True


	def get_users_id(self):
		return self.model.user_id


	def get_all_users(self):
		query = 'SELECT * FROM users'
		self.db.cursor.execute(query)

		users = self.db.cursor.fetchall()
		self.db.connection.commit()

		return users

