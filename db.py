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


	def __del__(self):
		self.connection.close()
