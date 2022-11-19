import json

class BooksDAO():

    def load_data(self):
        with open("books.json", "r", encoding="utf-8") as file:
           books_data = json.load(file)
        return books_data

    def get_all(self):
        return self.load_data()

    def get_by_pk(self, book_pk):
        books = self.load_data()
        for book in books:
            if book["pk"] == book_pk:
                return book



