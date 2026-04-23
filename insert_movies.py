import pymongo

def add_movie(movie_id, title, genres, database_name="movie_data", collection_name="movies"):
    """
    Adds a movie to the MongoDB "movies" collection in the movie_data database

    Args:
        movie_id (int): The unique ID number of the movies
        title (str): Title of the movie
        genres (str): Single string which lists the genres of the movie separated by pipe
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection of which I want to add new data, which is movies
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    movie_collection = movie_database[collection_name]

    # Create a document with the movie fields and the values I want to add for each field
    movie_document = {
        "movieId": movie_id,
        "title": title,
        "genres": genres
    }

    # Insert the document into the movies collection
    movie_collection.insert_one(movie_document)
    print(f"Movie '{title}' (ID: {movie_id}) added to the database.")


def main():
    """
    Main function to add five movies to the "movies" collection
    """
    add_movie(101010, "Train To Busan (2016)", "Thriller|Drama|Horror")
    add_movie(101011, "A Minecraft Movie (2025)", "Adventure|Comedy|Action")
    add_movie(101012, "Gladiator II (2024)", "History|Drama|Action")
    add_movie(101013, "Mickey 17 (2025)", "Action|Adventure|Comedy|Sci-fi")
    add_movie(101014, "Monkey Man (2024)", "Thriller|Action|Drama")
    print("Successfully inserted all of the movies")


if __name__ == "__main__":
    main()
