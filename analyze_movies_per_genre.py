import pymongo

def get_movies_per_genre(database_name="movie_data", collection_name="movies"):
    """
    Function that uses an aggregation pipeline to extract each genre from the genres string in the movies collection;
    the pipeline counts the amount of times each genre is seen in the collection

    Args:
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection in which I want to extract information from

    Returns:
        list: A list of dictionaries; each dictionary contains the genre and the number of movies per genre
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    movie_collection = movie_database[collection_name]

    # Create an aggregation pipeline to extract each genre individually from the genres field
    # Count the number of times each genre appears
    pipeline = [
        {
            "$project": {
                "genres": {
                    "$split": ["$genres", "|"]
                },
                "_id": 0
            }
        },
        {
            "$unwind": "$genres"
        },
        {
            "$group": {
                "_id": "$genres",
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "genre": "$_id",
                "count": 1,
                "_id": 0
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]
    # Get the movie-genre count information from the pipeline and return them
    genre_results = list(movie_collection.aggregate(pipeline))
    return genre_results

def main():
    """
    Main function that prints the number of movies per genre using the pipeline above
    """
    genre_results = get_movies_per_genre()
    print("Number of movies per genre:")
    for result in genre_results:
        print(f"Genre: {result['genre']}, Count: {result['count']}")

if __name__ == "__main__":
    main()
