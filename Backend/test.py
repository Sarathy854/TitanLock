from flask import Flask, jsonify 


app = Flask(__name__)


class book:
   def __init__(self, book_id, author, price):
     self.book_id = book_id
     self.author = author
     self.price = price

   def to_dict(self):
      return {"Book ID": self.book_id, "Author": self.author, "Price": self.price}

# Creating 4 Book objects
books = [
    book(101, "j.k.Rowling", 499.09),
    book(102, "George orwell", 599.60),
    book(103, "Agatha Christie", 699.70),
    book(104,"Dan Brown",599.25),
    
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in books])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
