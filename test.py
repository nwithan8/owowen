from owowen import API, SortDirection

api = API()
movie = api.get_random_wow(count=1)

print(movie[0].year)

movies = api.get_random_wow(count=3)
print(movies[0].year)

movie = api.get_chronological_wows(start=1)
print(movie[0].year)

movie = api.get_chronological_wows(start=1, end=3)
print(movie[2].year)

movie_titles = api.get_all_movies()
print(movie_titles)

directors = api.get_all_directors()
print(directors)


movie = api.get_random_wow(count=1)

print(movie[0].video.link_1080p)

