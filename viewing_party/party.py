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
def get_friends_movies(user_data):
    """
    Helper function to get a set of movie titles that the user's friends have watched.

    Args:
        user_data (dict): A dictionary containing the user's information. 
                        It has the following structure:
                        - 'watched': A list of dictionaries, each representing a movie 
                        the user has watched (with 'title', 'genre', and 'rating' keys).
                        - 'friends': A list of dictionaries, where each dictionary represents a friend. 
                        Each friend has a 'watched' key, which is a list of movies they have watched 
                        (with 'title', 'genre', and 'rating' keys).

    Returns:
        set: A set of movie titles (strings) that the user's friends have watched.

    Written by: Mariya Mokrynska
    """
    friends_watched_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])

    return friends_watched_titles


def get_unique_watched(user_data):
    """
    Returns a list of movies that the user has watched but none of their friends have watched.

    Args:
        user_data (dict): A dictionary containing the user's information. 
                        It has the following structure:
                        - 'watched': A list of dictionaries, each representing a movie 
                        the user has watched (with 'title', 'genre', and 'rating' keys).
                        - 'friends': A list of dictionaries, where each dictionary represents a friend. 
                        Each friend has a 'watched' key, which is a list of movies they have watched 
                        (with 'title', 'genre', and 'rating' keys).

    Returns:
        list: A list of dictionaries, each representing a movie that the user has watched, 
            but none of their friends have watched.

    Written by: Mariya Mokrynska
    """
    unique_movies_list = []
    friends_watched_titles = get_friends_movies(user_data)
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_titles:
            unique_movies_list.append(movie)

    return unique_movies_list


def get_user_movies(user_data):
    """
    Helper function to get a set of movie titles that the user has watched.

    Args:
        user_data (dict): A dictionary containing the user's information. 
                        It has the following structure:
                        - 'watched': A list of dictionaries, each representing a movie 
                        the user has watched (with 'title', 'genre', and 'rating' keys).

    Returns:
        set: A set of movie titles (strings) that the user has watched.

    Written by: Mariya Mokrynska
    """
    user_watched_titles = set()

    for movie in user_data["watched"]:
        user_watched_titles.add(movie["title"])

    return user_watched_titles


def get_friends_unique_watched(user_data):
    """
    Returns a list of movies that at least one of the user's friends has watched, 
    but the user has not watched.

    Args:
        user_data (dict): A dictionary containing the user's information. 
                        It has the following structure:
                        - 'watched': A list of dictionaries, each representing a movie 
                        the user has watched (with 'title', 'genre', and 'rating' keys).
                        - 'friends': A list of dictionaries, where each dictionary represents a friend. 
                        Each friend has a 'watched' key, which is a list of movies they have watched 
                        (with 'title', 'genre', and 'rating' keys).

    Returns:
        list: A list of dictionaries, each representing a movie that at least one of the user's 
            friends has watched, but the user has not watched.

    Written by: Mariya Mokrynska
    """
    friends_unique_movies_list = []
    user_watched_titles = get_user_movies(user_data)
    previous_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles and movie["title"] not in previous_titles:
                friends_unique_movies_list.append(movie)
                previous_titles.add(movie["title"])

    return friends_unique_movies_list

    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
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