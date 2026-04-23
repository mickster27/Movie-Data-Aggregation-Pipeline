import pymongo
import csv

def import_csv_to_mongodb(csv_file_path, collection_name, database_name="movie_data"):
    """
    Reads a given CSV file and inserts the data from the file into a collection in MongoDB

    Args:
        csv_file_path (str): The CSV file path
        collection_name (str): Name of the collection in MongoDB
        database_name (str): Name of the database in MongoDB
    """

    # Connect MongoDB to my server using pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Specify the database name
    movie_database = client[database_name]
    # Specify the collection name
    collection = movie_database[collection_name]

    # Read the CSV file and insert data into my MongoDB database
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Create a dictionary to hold each row of data separately
        csv_data_dictionary = []
        # For-loop that reads through each row of the CSV
        for row in reader:
            # Convert movieId values to int
            if 'movieId' in row:
                row['movieId'] = int(row['movieId'])
            # Convert userId values to int
            if 'userId' in row:
                row['userId'] = int(row['userId'])
            # Convert rating values to float
            if 'rating' in row:
                row['rating'] = float(row['rating'])
            # Insert the row of data into the dictionary
            csv_data_dictionary.append(row)

        # Insert the data into the collection
        collection.insert_many(csv_data_dictionary)
        print(f"{len(csv_data_dictionary)} records inserted into '{collection_name}'.")


def main():
    """
    Main function to set the file paths and call the import function for each file
    """
    # Specify the file paths
    movies_file_path = r"C:\Users\mikoc\Downloads\movies.csv"
    ratings_file_path = r"C:\Users\mikoc\Downloads\ratings.csv"
    tags_file_path = r"C:\Users\mikoc\Downloads\tags.csv"

    # Import the data
    import_csv_to_mongodb(movies_file_path, "movies")
    import_csv_to_mongodb(ratings_file_path, "ratings")
    import_csv_to_mongodb(tags_file_path, "tags")

    print("Successfully inserted all the data into MongoDB from the CSV files")


if __name__ == "__main__":
    main()
