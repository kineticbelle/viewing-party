# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    
    if all([title, genre, rating]):
        return {"title": title, "genre": genre, "rating": rating}
        
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    
    total_rating = 0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    
    return total_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    if user_data["watched"] is None:
        return None
        
    genre_avg = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_avg:
            genre_avg[genre] += 1
        else: 
            genre_avg[genre] = 1

    most_watched_genre = None
    max_count = 0

    for genre, count in genre_avg.items():
        if count > max_count:
            most_watched_genre = genre
            max_count = count  
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    if not most_watched_genre:
        return []
    
    rec_movies = []
    watched_titles = {movie["title"] for movie in user_data["watched"]}
    seen_movies = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (
                movie["genre"] == most_watched_genre and 
                movie["title"] not in watched_titles and
                movie["title"] not in seen_movies
            ):
                rec_movies.append(movie)
                seen_movies.add(movie["title"])
    return rec_movies


def get_rec_from_favorites(user_data):
    rec_movies = []

    for movie in user_data["favorites"]:
        movie_in_favorites = True

        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                movie_in_favorites = False
                break
        
        if movie_in_favorites:
            rec_movies.append(movie)

    return rec_movies