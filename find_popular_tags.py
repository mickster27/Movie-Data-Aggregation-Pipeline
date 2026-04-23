import pymongo

def get_movies_per_tag(database_name="movie_data", collection_name="tags"):
    """
    Function that uses an aggregation pipeline to count the number of times a tag appears in the tags collection;
    Then outputs the most popular tag that appears the most in the collection

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

    # Create an aggregation pipeline the counts the number of times a tag appears
    pipeline = [
        {
            "$group": {
                "_id": "$tag",
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "tag": "$_id",
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

    # Get the tags count information from the pipeline and return them
    tag_results = list(tag_collection.aggregate(pipeline))
    return tag_results


def main():
    """
    Main function to that prints the most popular tag of the collection, which is the 0th index of the dictionary
    """
    tag_results = get_movies_per_tag()
    most_popular_tag = tag_results[0]['tag']
    print(f"The most popular tag is: {most_popular_tag}")


if __name__ == "__main__":
    main()
