from projections_controller import ProjectionController


class ProjectionView:
	def __init__(self):
		self.controller = ProjectionController()


	def insert_new_projection(self):
		movie_id = int(input('Movie id: '))
		projection_type = input('Type of the projection: ')
		date = input('Date(yyyy-mm-dd): ')
		time = input('Time(00:00): ')
		self.controller.add_projection(movie_id=movie_id, projection_type=projection_type, date=date, time=time)


	def choose_projection_by_id(self):
		projection_id = int(input('Choose the id for the projection you want: '))
		projection = self.controller.get_projection_by_id(projection_id=projection_id)

		while projection is False:
			print('No projection with that id. Try again')
			projection_id = int(input('> '))
			projection = self.controller.get_projection_by_id(projection_id=projection_id)


	def show_projections_for_the_chosen_movie(self, movie_id):
		answer = input('Do you want to choose a date? y/n: ')

		if answer is 'y':
			date = input('Date: ')
			projections = self.controller.get_projections_by_movie_id_and_date(movie_id=movie_id, date=date)
		else:
			projections = self.controller.get_projections_by_movie_id(movie_id=movie_id)

		print('All current projections for the movie:\n')
		for projection in projections:
			print(f'[{projection[0]}] - {projection[2]} {projection[3]} {projection[4]}')


	def show_all_projections(self):
		print('All current projections\n')
		projections = self.controller.get_all_projections()
		for projection in projections:
			print(f'[{projection[0]}] - [{projection[1]}] {projection[2]} {projection[3]} {projection[4]}')
