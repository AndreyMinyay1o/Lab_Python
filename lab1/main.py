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

# Класс Reader (Читатель)
class Reader:
    def __init__(self, reader_id, name, address, phone):
        self._reader_id = reader_id
        self._name = name
        self._address = address
        self._phone = phone
        self._validate_fields()

    def _validate_field(self, value, expected_type, error_message, min_length=None):
        if not isinstance(value, expected_type):
            raise ValueError(error_message)
        if min_length and len(value) < min_length:
            raise ValueError(error_message)

    def _validate_phone(self, phone):
        if not re.match(r"^\+?[0-9]{10,15}$", phone):
            raise ValueError("Phone number must be in a valid format.")
    
    def _validate_fields(self):
        self._validate_field(self._reader_id, int, "Reader ID must be a valid integer.")
        self._validate_field(self._name, str, "Name must be at least 3 characters long.", min_length=3)
        self._validate_field(self._address, str, "Address must be at least 5 characters long.", min_length=5)
        self._validate_phone(self._phone)

    def __str__(self):
        return f"Reader(ID: {self._reader_id}, Name: {self._name}, Address: {self._address}, Phone: {self._phone})"

class Borrow:
    def __init__(self, borrow_id, book_id, reader_id, date_borrowed, date_returned):
        self._borrow_id = borrow_id
        self._book_id = book_id
        self._reader_id = reader_id
        self._date_borrowed = date_borrowed
        self._date_returned = date_returned

