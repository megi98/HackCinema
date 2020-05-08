from movie_controller import MovieController


class MovieView:
	def __init__(self):
		self.controller = MovieController()


	def get_movie_by_id(self, id):
		title = self.controller.get_movie_by_id(id)
		return title


	def show_all_movies(self):
		movies = self.controller.show_all_movies()
		print('Current movies:')

		for movie in movies:
			print(f'[{movie[0]}] - {movie[1]} ({movie[2]})')


	def show_projections_by_movie_id(self, movie_id):
		projections = self.controller.get_projections_by_movie_id(movie_id)
		print(f"Projections for movie '{self.get_movie_by_id(movie_id)}'")

		for projection in projections:
			print(f'[{projection[0]}] - {projection[3]} {projection[4]} ({projection[2]})')


	def show_projections_by_movie_id_and_date(self, movie_id, date):
		projections = self.controller.get_projections_by_movie_id_and_date(movie_id, date)
		print(f"Projections for movie '{self.get_movie_by_id(movie_id)}' on date {date}:")

		for projection in projections:
			print(f'[{projection[0]}] - {projection[4]} ({projection[2]})')


	def show_all_projections(self):
		projections = self.controller.get_all_projections()
		print('All projections:')

		for projection in projections:
			print(f'[{projection[0]}] [{projection[1]}] - {projection[3]} {projection[4]} ({projection[2]})')
