import json
import os

class DatabaseQuery:
    def __init__(self, json_path):
        self.json_path = json_path

    def get_book_location(self, book_title):
        """
        Retrieve the location of a book given its title.
        Args:
            book_title (str): The title of the book to search for.
        Returns:
            str: The location of the book or an error message.
        """
        try:
            with open(self.json_path, 'r') as file:
                data = json.load(file)
            
            book_info = data.get(book_title)
            if book_info:
                return book_info.get("location", "Location not specified")
            else:
                return "Book not found"
        except Exception as e:
            return f"Error: {str(e)}"
