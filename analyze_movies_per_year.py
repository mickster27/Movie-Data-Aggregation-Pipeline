import pymongo


def get_movies_per_year(database_name="movie_data", collection_name="movies"):
    """
    Function that uses an aggregation pipeline to extract the release year from the move title
    and counts and outputs the amount of movies released from each year

    Args:
        database_name (str): The name of the database in MongoDB
        collection_name (str): The name of the collection in which I want to extract information from

    Returns:
        list: A list of dictionaries; each dictionary contains the year and the number of movies
              released in that year
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    movie_collection = movie_database[collection_name]

    # Create the aggregation pipeline to extract the year from the title and count the number of movies released
    # per year
    pipeline = [
        {
            "$match": {
                "title": {"$regex": "\\((19|20)\\d{2}\\)$"}
            }
        },
        {
            "$project": {
                "year": {
                    "$toInt": {
                        "$substr": [
                            "$title",
                            {"$subtract": [{"$strLenBytes": "$title"}, 5]},
                            4
                        ]
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$year",
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "year": "$_id",
                "count": 1,
                "_id": 0
            }
        },
        {
            "$sort": {"year": -1}
        }
    ]
    # Get the movie-year count from the pipeline and return them
    year_results = list(movie_collection.aggregate(pipeline))
    return year_results


def main():
    """
    Main function that prints the number of movies released for every year using the pipeline above
    """
    year_results = get_movies_per_year()
    print("Number of movies released per year:")
    for result in year_results:
        print(f"Year: {result['year']}, Count: {result['count']}")


if __name__ == "__main__":
    main()
