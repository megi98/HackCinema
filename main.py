from user_view import UserView
from movies_view import MovieView
from projections_view import ProjectionView
from reservations_view import ReservationView



def main():
	user_v = UserView()
	movies_v = MovieView()
	projections_v = ProjectionView()
	reservation_v = ReservationView()

	command = user_v.welcome()
	if command == 1:
		user_v.login()
	else:
		user_v.signup()
	user_id = user_v.controller.get_users_id()

	movies_v.show_all_movies()
	movies_v.choose_movie_by_id()
	movie_id = movies_v.controller.gateway.model.movie_id

	projections_v.show_projections_for_the_chosen_movie(movie_id=movie_id)
	projections_v.choose_projection_by_id()
	projection_id = projections_v.controller.gateway.model.projection_id

	reservation_v.show_available_seats_count(projection_id=projection_id)
	reservation_v.show_map_for_projection(projection_id=projection_id)
	reservation_v.make_reservation(user_id=user_id, projection_id=projection_id)


if __name__ == '__main__':
	main()