from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.validators.forms import SearchBookForm
from app.models.book import Book

api = Redprint('book')


@api.route('/search')
def search():
    # request.args.to_dict()
    form = SearchBookForm().validate_form_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter(isbn=isbn).first_or_404()
    return jsonify(book)