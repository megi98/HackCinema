from movie_controller import MovieController


class MovieView:
	def __init__(self):
		self.controller = MovieController()


	def get_movie_by_id(self, id):
		title = self.controller.get_movie_by_id(id)
		return title


	def show_all_movies(self):
		movies = self.controller.show_all_movies()

		for movie in movies:
			print(f'[{movie[0]}] - {movie[1]} ({movie[2]})\n')


	def show_projections_by_movie_id(self, movie_id):
		projections = self.controller.get_projections_by_movie_id(movie_id)

		for projection in projections:
			print(f'{projection[0]} | {projection[1]} | {projection[2]} | {projection[3]} | {projection[4]}\n')


	def show_projections_by_movie_id_and_date(self, movie_id, date):
		projections = self.controller.get_projections_by_movie_id_and_date(movie_id, date)

		for projection in projections:
			print(f'{projection[0]} | {projection[1]} | {projection[2]} | {projection[3]} | {projection[4]}\n')


	def show_all_projections(self):
		projections = self.controller.get_all_projections()

		for projection in projections:
			print(f'{projection[0]} | {projection[1]} | {projection[2]} | {projection[3]} | {projection[4]}\n')


mv = MovieView()
mv.show_all_movies()