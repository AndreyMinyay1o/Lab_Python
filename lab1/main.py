import json
import re

# Классы для модели библиотеки
class Book:
    def __init__(self, book_id, title, author, year, isbn, genre):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._year = year
        self._isbn = isbn
        self._genre = genre

class Reader:
    def __init__(self, reader_id, name, address, phone):
        self._reader_id = reader_id
        self._name = name
        self._address = address
        self._phone = phone

class Borrow:
    def __init__(self, borrow_id, book_id, reader_id, date_borrowed, date_returned):
        self._borrow_id = borrow_id
        self._book_id = book_id
        self._reader_id = reader_id
        self._date_borrowed = date_borrowed
        self._date_returned = date_returned

