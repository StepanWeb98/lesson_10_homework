from flask import Flask, render_template
from books_dao import BooksDAO

app = Flask(__name__)
books_dao = BooksDAO()

@app.route("/home")
def page_index():
  books = books_dao.get_all()
  return render_template("index.html", books=books)

@app.route("/books/<int:pk>")
def page_skill(pk):
    book = books_dao.get_by_pk(pk)
    return render_template("books.html", book=book)


app.run()
