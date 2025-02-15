#Напишите функцию, которая берет один фильм и возвращает, если его оценка IMDB выше 5.5True pytihon
def check_movie_rating(movie):
    
    if movie.get('imdb_rating') > 5.5:
        return True
    else:
        return False

movie = {'title': 'Movie Title', 'imdb_rating': 6.2}
result = check_movie_rating(movie)
print(result) 

#Напишите функцию, которая возвращает подсписок фильмов с оценкой IMDB выше 5,5
def filter_movies_by_rating(movies):
    
    filtered_movies = [movie for movie in movies if movie.get('imdb_rating', 0) > 5.5]
    return filtered_movies


movies = [
    {'title': 'Movie 1', 'imdb_rating': 6.2},
    {'title': 'Movie 2', 'imdb_rating': 4.5},
    {'title': 'Movie 3', 'imdb_rating': 7.8},
    {'title': 'Movie 4', 'imdb_rating': 5.0}
]

result = filter_movies_by_rating(movies)
print(result)  

#Напишите функцию, которая принимает имя категории и возвращает только те фильмы, которые относятся к этой категории.
def filter_movies_by_category(movies, category_name):
    
    filtered_movies = [movie for movie in movies if category_name in movie.get('category', [])]
    return filtered_movies

movies = [
    {'title': 'Movie 1', 'imdb_rating': 6.2, 'category': ['Action', 'Thriller']},
    {'title': 'Movie 2', 'imdb_rating': 4.5, 'category': ['Drama', 'Romance']},
    {'title': 'Movie 3', 'imdb_rating': 7.8, 'category': ['Action', 'Adventure']},
    {'title': 'Movie 4', 'imdb_rating': 5.0, 'category': ['Comedy']},
    {'title': 'Movie 5', 'imdb_rating': 6.1, 'category': ['Action']}
]

result = filter_movies_by_category(movies, 'Action')
print(result)

#Напишите функцию, которая берет список фильмов и вычисляет средний балл IMDB.
def calculate_average_imdb_rating(movies):

    total_rating = sum(movie.get('imdb_rating', 0) for movie in movies)
    num_movies = len(movies)
    
  
    if num_movies > 0:
        average_rating = total_rating / num_movies
        return average_rating
    else:
        return 0 

movies = [
    {'title': 'Movie 1', 'imdb_rating': 6.2},
    {'title': 'Movie 2', 'imdb_rating': 4.5},
    {'title': 'Movie 3', 'imdb_rating': 7.8},
    {'title': 'Movie 4', 'imdb_rating': 5.0}
]

result = calculate_average_imdb_rating(movies)
print(result)  

#Напишите функцию, которая принимает категорию и вычисляет средний балл IMDB.
def calculate_average_rating_by_category(movies, category_name):

    filtered_movies = [movie for movie in movies if category_name in movie.get('category', [])]
    
 
    if filtered_movies:
        total_rating = sum(movie.get('imdb_rating', 0) for movie in filtered_movies)
        average_rating = total_rating / len(filtered_movies)
        return average_rating
    else:
        return 0  

movies = [
    {'title': 'Movie 1', 'imdb_rating': 6.2, 'category': ['Action', 'Thriller']},
    {'title': 'Movie 2', 'imdb_rating': 4.5, 'category': ['Drama', 'Romance']},
    {'title': 'Movie 3', 'imdb_rating': 7.8, 'category': ['Action', 'Adventure']},
    {'title': 'Movie 4', 'imdb_rating': 5.0, 'category': ['Comedy']},
    {'title': 'Movie 5', 'imdb_rating': 6.1, 'category': ['Action']}
]

result = calculate_average_rating_by_category(movies, 'Action')
print(result)  


