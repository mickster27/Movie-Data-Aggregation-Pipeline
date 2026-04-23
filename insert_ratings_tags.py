import pymongo

def add_rating(user_id, movie_id, rating, database_name="movie_data", collection_name="ratings"):
    """
    Function that inserts a tag in the ratings collection of the movies_data database

    Args:
        user_id (int): My user ID
        movie_id (int): The ID of the movie being rated
        rating (float): A float value of the movie rating
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection of which I want to add new data, which is ratings
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    ratings_collection = movie_database[collection_name]

    # Create a document with the rating's fields and the values I want to add for each field
    rating_document = {
        "userId": user_id,
        "movieId": movie_id,
        "rating": rating
    }

    # Insert the document into the ratings collection
    ratings_collection.insert_one(rating_document)
    print(f"Rating {rating} added for movieId {movie_id} by userId {user_id}.")


def add_tag(user_id, movie_id, tag, database_name="movie_data", collection_name="tags"):
    """
    Function that inserts a tag in the tags collection of the movies_data database

    Args:
        user_id (int): My user ID
        movie_id (int): The ID of the movie being tagged.
        tag (str): The string of the tag I want to add in the database
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection of which I want to add new data, which is tags
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    tags_collection = movie_database[collection_name]

    # Create a document with the tag's fields and the values I want to add for each field
    tag_document = {
        "userId": user_id,
        "movieId": movie_id,
        "tag": tag
    }

    # Insert the document into the tags collection
    tags_collection.insert_one(tag_document)
    print(f"Tag '{tag}' added for movieId {movie_id} by userId {user_id}.")


def main():
    """
    Main function to add ratings and tags for the five movies that I previously added
    """
    # My unique userID that I want to use
    user_id = 2727

    # Add 5 ratings that correspond to the movies that I previously added
    add_rating(user_id, 101010, 4.5)  # Train to Busan
    add_rating(user_id, 101011, 4.0)  # A Minecraft Movie
    add_rating(user_id, 101012, 4.4)  # Gladiator II
    add_rating(user_id, 101013, 4.3)  # Mickey 17
    add_rating(user_id, 101014, 4.6)  # Monkey Man

    # Add 5 tags that correspond to the movies that I previously added
    add_tag(user_id, 101010, "zombie")      # Train to Busan
    add_tag(user_id, 101011, "game")        # A Minecraft Movie
    add_tag(user_id, 101012, "rome")        # Gladiator II
    add_tag(user_id, 101013, "outer-space") # Mickey 17
    add_tag(user_id, 101014, "revenge")     # Monkey Man
    print("Successfully inserted all of the ratings and tags")


if __name__ == "__main__":
    main()
