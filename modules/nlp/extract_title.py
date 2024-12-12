import os
import openai

class NLPModule:
    def __init__(self, api_key, database):
        """
        Initialize the NLP module with OpenAI API key and book database.
        """
        self.api_key = api_key
        openai.api_key = self.api_key
        self.database = database

    def process_text(self, text):
        """
        Processes the input text to determine book search intent.
        Args:
            text (str): User input text.
        Returns:
            dict: Book details if found, else a not found message.
        """
        try:
            # Use OpenAI API to extract book title
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Identify the book title from this query: '{text}'. Return only the title.",
                max_tokens=50,
                temperature=0.5,
            )
            book_title = response["choices"][0]["text"].strip()
            
            # Search the book database
            if book_title in self.database:
                return {
                    "status": "success",
                    "data": self.database[book_title],
                }
            else:
                return {
                    "status": "not_found",
                    "message": f"The book '{book_title}' was not found in the database."
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

nlp = NLPModule(api_key=os.getenv("OPENAI_API_KEY"), database=str)

user_input = "Can you help me find Clean Code?"
result = nlp.process_text(user_input)

if result["status"] == "success":
    print("Book found!")
    print("Location:", result["data"]["location"])
else:
    print(result["message"])
