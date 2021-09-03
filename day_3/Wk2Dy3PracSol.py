# ITP Week 2 Day 3 (In-Class) Practice
my_movies = ["The Godfather", "Ace Ventura", "Gigli", "Die Hard"]

new_releases = ["Encino Man", "I know what you did last Summer", "Phantom Menace"]

def movie_listing(movies):
    for movie in movies:
        print(movie)
movie_listing(my_movies)

def update_movies(new_movies):
    for movie in new_movies:
        my_movies.append(movie)
update_movies(new_releases)
print(my_movies)