import sys
import os
import json

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from modules.db_querying.db_query import DatabaseQuery

def main():
    # Load book data from JSON file
    json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../database/books.json'))
    
    db_query = DatabaseQuery(json_path)
    
    book_title = "Clean Code"
    location = db_query.get_book_location(book_title)
    print(f"Location of '{book_title}': {location}")

if __name__ == "__main__":
    main()
