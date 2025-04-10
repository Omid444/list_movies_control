import statistics
from statistics import median
import random
import matplotlib
import matplotlib.pyplot as plt

def show_menu():
    menu = '''Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram'''
    print(menu)

def choice_menu():
    menu_num =int(input('\nEnter Choice (1-8): '))
    return menu_num

def show_movie_list(movies_list):
    for movie, rate in movies_list.items():
        print(f'{movie}:{rate}')

def add_movie(movies_list):
    movie_name = (input('Enter movie name: ')).lower()
    movie_rate = float(input('Enter movie rating: '))
    movies_list[movie_name.title()] = movie_rate
    print(f'your movie {movie_name} added successfully')


def delete_movie(movies_list):
    movie_name = (input('Enter movie name: ')).lower()
    if movie_name.title() in movies_list:
        movies_list.pop(movie_name.title())
        print(f'your movie {movie_name} deleted successfully')
    else:
        print(f'The movie {movie_name} does not exist')


def update_movie(movies_list):
    movie_name = (input('Enter movie name: ')).lower()
    if movie_name.title() in movies_list:
        movie_rate = float(input('Enter new movie rating: '))
        movies_list[movie_name.title()] = movie_rate
        print('New rating successfully updated')
    else:
        print(f'The movie {movie_name.capitalize()} does not exist')


def find_best_movies(movies_list):
    best_movies = []
    best_movie_rate = max(movies_list.values())
    for movie, rate in movies_list.items():
        if rate == best_movie_rate:
            best_movies.append((movie, rate))

    return best_movies


def find_worst_movie(movies_list):
    worst_movies = []
    worst_movie_rate = min(movies_list.values())
    for movie, rate in movies_list.items():
        if rate == worst_movie_rate:
            worst_movies.append((movie, rate))

    return worst_movies

def calculate_average_rating(movies_list):
    return statistics.mean(movies_list.values())


def  calculate_median_rate(movies_list):
    return median(list(movies_list.values()))


def show_stats(movies_list):

    best_movies = find_best_movies(movies_list)

    worst_movies = find_worst_movie(movies_list)

    average_rating = calculate_average_rating(movies_list)

    median_rate = calculate_median_rate(movies_list)

    print(f'Average rating: {average_rating:.2f}\n')
    print(f'Median rating: {median_rate}\n')
    for movie in best_movies:
        print(f'The best movie: {movie[0]}:{movie[1]}')
    print()
    for movie in worst_movies:
        print(f'The worst movie: {movie[0]}:{movie[1]}')


def show_random_movie(movies_list):
    random_movie = random.choice(list(movies_list.items()))
    print(f'{random_movie[0]}:{random_movie[1]}')


def search_movie(movies_list):
    user_input = input('Enter movie name: ').lower()
    for movie, rate in movies_list.items():
        if user_input in movie.lower():
            print(f'{movie}:{rate}')

def get_value(item):
    return item[1]

def sort_movie_by_rating(movies_list):
    sorted_dic = dict(sorted(movies_list.items(),key=get_value , reverse= True))
    for movie , rate in sorted_dic.items():
        print(f'{movie}:{rate}')

def show_histogram(movies_list):
    rating_list = list(movies_list.values())
    plt.hist(rating_list)
    plt.show()

def control_menu(number_selected, list_of_movies):

    menu_dict = {1:show_movie_list,2:add_movie, 3:delete_movie, 4:update_movie, 5:show_stats, 6:show_random_movie, 7:search_movie, 8:sort_movie_by_rating, 9:show_histogram}
    for menu_number, menu in menu_dict.items():
        if menu_number == number_selected:
            menu(list_of_movies)

def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    # Your code here
    print('********** My Movies Database **********')
    condition = True
    while condition:
        show_menu()
        menu_number = choice_menu()
        control_menu(menu_number, movies)
        user_input = input('\nPress Enter to continue ')
        if user_input =='' or user_input.isspace():
            condition = True
        else:
            condition = False




if __name__ == "__main__":
    main()
