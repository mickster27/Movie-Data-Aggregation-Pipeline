# MongoDB Data Aggregation Pipeline

This project is a Python-based data engineering pipeline designed to extract, transform, and analyze a large-scale movie dataset using MongoDB. It demonstrates the ability to build ETL (Extract, Transform, Load) workflows and utilize the MongoDB Aggregation Framework to run complex analytical queries on non-relational data.

## Project Purpose
The goal of this project was to manipulate and analyze raw CSV data (movies, user ratings, and tags) by migrating it into a NoSQL document database. Once migrated, the objective was to write highly efficient aggregation pipelines to uncover insights, such as rating distributions, popular genres, and chronological release trends, without relying on traditional SQL joins.

## Technologies Used
* **Language:** Python
* **Database:** MongoDB
* **Libraries:** PyMongo, CSV

## Key Functionalities
* **Data Loading:** Reads local CSV datasets, formats data types, and inserts thousands of records into MongoDB.
* **String Manipulation:** Utilizes Regex and substring operations within database queries to dynamically extract data (e.g., isolating release years from title strings).
* **Data Analytics:** Executes multi-stage aggregation pipelines to calculate:
  * Total number of movies released per year
  * The most popular user-generated tags
  * The exact distribution of movie ratings across the platform
  * The count of movies available per genre

## My Role and Contributions
As the sole developer for this project, I engineered the entire pipeline from scratch. My responsibilities included writing the Python scripts to connect and authenticate with the local MongoDB server, designing the NoSQL document structures for insertion, and writing the specific aggregation queries required to transform and analyze the data payloads.

## How to Run

### Prerequisites
* Python 3 installed
* A local instance of MongoDB running on `mongodb://localhost:27017/`
* `pymongo` installed (`pip install pymongo`)

### Execution Order
1. **Load the Data:** Update the file paths in `csv_to_mongo.py` to point to your local CSV files, then run the script to populate your database.
2. **Seed Additional Data:** Run `insert_movies.py` and `insert_movies_tags.py` to insert test documents into the collections.
3. **Run Analytics:** Execute any of the analytics scripts (e.g., `analyze_movies_per_year.py` or `find_popular_tags.py`) in your terminal to view the aggregation results printed directly to the console.

## 🧠 Lessons Learned
Developing this pipeline provided deep, hands-on experience with NoSQL database architecture. A major takeaway was learning how to efficiently chain MongoDB aggregation stages (`$match`, `$project`, `$group`, `$sort`) to perform complex data transformations on the database server side, rather than loading massive amounts of raw data into Python memory to process it. It also reinforced the importance of cleaning and formatting data types during the initial ETL load phase.
