import pymongo

def count_movies_tagged(database_name="movie_data", collection_name="tags"):
    """
    Function that uses an aggregation pipeline to count the number of times a tag appears in the tags collection

    Args:
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection in which I want to extract information from

    Returns:
        list: A list of dictionaries; each dictionary contains a tag and the number of times the tag appears
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    tag_collection = movie_database[collection_name]

    # Create an aggregation pipeline to count how many movies have at least one tag
    pipeline = [
        {
            "$group": {
                "_id": "$movieId"
            }
        },
        {
            "$count": "number_of_tagged_movies"
        }
    ]
    # Get the amount of movies that have been tagged using the pipeline above and return the result
    movies_tagged_count = list(tag_collection.aggregate(pipeline))
    return movies_tagged_count[0]["number_of_tagged_movies"]


def main():
    """
    Main function that prints the number of times a unique tag appears using the pipeline above
    """
    movies_tagged_count = count_movies_tagged()
    print(f"Number of movies that have been tagged: {movies_tagged_count}")


if __name__ == "__main__":
    main()
