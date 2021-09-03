# ITP Week 2 Day 3 (In-Class) Practice
my_movies = ["The Godfather", "Ace Ventura", "Gigli", "Die Hard"]

new_releases = ["Encino Man", "I know what you did last Summer", "Phantom Menace"]

#Create a function defined as "movie_listing" which takes one parameter, called "movies".  Write a function that will loop through a list and print out each item.  Then call that function, passing it the my_movies list as an argument.
def movie_listing(movies):
    for movie in movies:
        print(movie)
movie_listing(my_movies)
#Define a function called "update_movies" that will loop through a list parameter, and use the insert() method on each item to the my_movies list.  Call that function using the new_releases list as the argument.  Then call the movie_listing function passing the "new_releases" as the argument.  It should print the updated list.

def update_movies(new_movies):
    for movie in new_movies:
        my_movies.append(movie)
update_movies(new_releases)
print(my_movies)