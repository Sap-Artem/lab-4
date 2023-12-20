class MovieRecommendation:
    def __init__(self, movies_file, history_file):
        self.movies = self.load_movies(movies_file)
        self.history = self.load_history(history_file)
    #загрузить фильм из файла
    def load_movies(self, movies_file):
        movies = {}
        with open(movies_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    movie_id, movie_name = line.split(',')
                    movies[int(movie_id)] = movie_name
        return movies
    #загрузить историю просмотров из файла
    def load_history(self, history_file):
        history = []
        with open(history_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    history.append([int(movie_id) for movie_id in line.split(',')])
        return history
    #главная функция по подбору рекомендации
    def recommend_movie(self, user_history):
        user_movies = set(user_history)
        #Поиск пользователей, у которых есть как минимум половина общих с пользователем фильмов
        candidate_users = [user for user in self.history if len(set(user) & user_movies) >= len(user) // 2]
        #Исключение фильмов, которые пользователь уже просмотрел
        candidate_movies = set()
        for user in candidate_users:
            for movie_id in user:
                if movie_id not in user_movies and movie_id in self.movies:
                    candidate_movies.add(movie_id)
        #Поиск фильма с максимальным количеством просмотров среди фильмов-кандидатов
        max_views = 0
        recommended_movie = None
        for movie_id in candidate_movies:
            views = sum([user.count(movie_id) for user in self.history])
            if views > max_views:
                max_views = views
                recommended_movie = movie_id
        if recommended_movie:
            return self.movies[recommended_movie]
        else:
            return "No recommendation available"

def main():
    movies_file = 'cinema.txt'
    history_file = 'cinema_history.txt'
    recommendation = MovieRecommendation(movies_file, history_file)
    user_input = input("Введите список просмотренных фильмов: ")
    user_history = [int(movie_id) for movie_id in user_input.split(',')]
    recommended_movie = recommendation.recommend_movie(user_history)
    print(recommended_movie)
if __name__ == "__main__":
    main()

