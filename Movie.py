class Movie:
    def __init__(self, movie_name, movie_country, series):
        self.movie_name = movie_name
        self.movie_country = movie_country
        self.series = series

    def genre(self):
        print("Psychological thriller")


class Series:
    def __init__(self, series_name, series_country):
        self.series_name = series_name
        self.series_country = series_country


series = Series("Penthouse", "Korea")
movie = Movie("Soulmate", "Korea", series)
print(movie.series.series_country)
movie.genre()

series1 = Series("Reset", "China")
movie1 = Movie("Jasmine", "China", series1)

print(movie1.series.series_name)