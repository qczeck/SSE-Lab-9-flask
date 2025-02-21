from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample book data
books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]


@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre')

    if genre:
        filtered_books = [book for book in books if book['genre'].lower() == genre.lower()]
        return jsonify(filtered_books)

    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
