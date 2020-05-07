import sqlite3

from settings import DB_NAME
from db_schema.movies import CREATE_MOVIES
from db_schema.projections import CREATE_PROJECTIONS
from db_schema.reservations import CREATE_RESERVATIONS
from db_schema.users import CREATE_USERS



class Database:
	def __init__(self):
		self.connection = sqlite3.connect(DB_NAME)
		self.cursor = self.connection.cursor()


	def create_tables(self):
		self.cursor.execute(CREATE_MOVIES)
		self.cursor.execute(CREATE_PROJECTIONS)
		self.cursor.execute(CREATE_RESERVATIONS)
		self.cursor.execute(CREATE_USERS)

		self.connection.commit()


	def add_movie(self, *, name, rating):
		query = f'''
		INSERT INTO movies (name, rating)
		  VALUES('{name}', {rating});
		'''

		self.cursor.execute(query)
		self.connection.commit()


	def get_movie_by_id(self, *, movie_id):
		query = f'''
		SELECT name, rating FROM movies
		  WHERE id = {movie_id};
		'''
		self.cursor.execute(query)

		movie = self.cursor.fetchone()
		self.connection.commit()

		return movie 


	def add_projection(self, *, movie_id, type, date, time):
		query = f'''
		INSERT INTO projections (movie_id, type, date, time)
		  VALUES({movie_id}, '{type}', '{date}', '{time}');
		'''

		self,cursor.execute(query)
		self.connection.commit()


	def show_movies(self):
		query = '''
		SELECT * FROM movies
		  ORDER BY rating DESC;
		'''
		self.cursor.execute(query)

		movies = self.cursor.fetchall()
		self.connection.commit()

		return movies


	def show_projections_by_movie_id(self, movie_id):
		query = f'''
		SELECT * FROM projections
		  WHERE movie_id = {movie_id}
		  ORDER BY date;
		'''
		self.cursor.execute(query)

		projections = self.cursor.fetchall()
		self.connection.commit()

		return projections


	def show_projections_by_movie_id_and_date(self, movie_id, date):
		query = f'''
		SELECT * FROM projections
		  WHERE movie_id = {movie_id} AND date LIKE '{date}'
		  ORDER BY date;
		'''
		self.cursor.execute(query)

		projections = self.cursor.fetchall()
		self.connection.commit()

		return projections


	def create_user(self, *, email, password):
		query = f'''
		INSERT INTO users (email, password)
		  VALUES('{email}', '{password}');
		'''

		self.cursor.execute(query)
		self.connection.commit()


	def get_user(self, *, email, password):
		query = f'''
		SELECT id, email FROM users
		  WHERE email = '{email}' AND password = '{password}';
		'''
		self.cursor.execute(query)

		user = self.cursor.fetchone()
		self.connection.commit()

		return user


	def make_reservation(self, *, user_id, projection_id, row, col):
		query = f'''
		INSERT INTO reservations (user_id, projection_id, row, col)
		  VALUES({user_id}, {projection_id}, {row}, {col})
		'''

		self.cursor.execute(query)
		self.connection.commit()


	def get_seats(self, *, projection_id):
		query = f'''
		SELECT row, col FROM reservations
		  WHERE projection_id = {projection_id};
		'''

		self.cursor.execute(query)
		seats = self.cursor.fetchall()
		self.connection.commit()

		return seats


	def __del__(self):
		self.connection.close()
		
