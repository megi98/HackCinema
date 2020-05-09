from movie_controller import MovieController


class MovieView:
	def __init__(self):
		self.controller = MovieController()


	def insert_new_movie(self):
		name = input('Title: ')
		rating = int(input('Rating: '))
		self.controller.add_movie(name=name, rating=rating)


	def choose_movie_by_id(self):
		movie_id = int(input('Choose the id for the movie you want: '))
		movie = self.controller.get_movie_by_id(movie_id=movie_id)

		while movie is False:
			print('No movie with that id. Try again')
			movie_id = int(input('> '))
			movie = self.controller.get_movie_by_id(movie_id=movie_id)

		print(f'Great choice!\nTitle: {movie[0]}\nRating: {movie[1]}')


	def show_all_movies(self):
		movies = self.controller.get_all_movies()
		print('Current movies:\n')

		for movie in movies:
			print(f'[{movie[0]}] - {movie[1]} ({movie[2]})')
