import pymongo

def get_movies_per_rating(database_name="movie_data", collection_name="ratings"):
    """
    Function that uses an aggregation pipeline to count the number of times a rating appears in the ratings collection

    Args:
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection in which I want to extract information from

    Returns:
        list: A list of dictionaries; each dictionary contains a rating and the number of times the rating appears
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    rating_collection = movie_database[collection_name]

    # Create an aggregation pipeline the counts the number of movies that have a given rating
    pipeline = [
        {
            "$group": {
                "_id": "$rating",
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "rating": "$_id",
                "count": 1,
                "_id": 0
            }
        },
        {
            "$sort": {
                "rating": 1
            }
        }
    ]
    # Get the movie-ratings count information from the pipeline and return them
    ratings_results = list(rating_collection.aggregate(pipeline))
    return ratings_results


def main():
    """
    Main function that prints the number of movies per rating using the pipeline above
    """
    ratings_results = get_movies_per_rating()
    print("Number of movies per rating:")
    for result in ratings_results:
        print(f"Rating: {result['rating']}, Count: {result['count']}")


if __name__ == "__main__":
    main()
