import re
import json

# Класс Book (Книга)
class Book:
    def __init__(self, book_id=None, title=None, author=None, year=None, isbn=None, genre=None, data=None):
        if data:
            self._from_json(data)
        else:
            self._book_id = book_id
            self._title = title
            self._author = author
            self._year = year
            self._isbn = isbn
            self._genre = genre
            self._validate_fields()

    def _from_json(self, data):
        data = json.loads(data)
        self._book_id = data["book_id"]
        self._title = data["title"]
        self._author = data["author"]
        self._year = data["year"]
        self._isbn = data["isbn"]
        self._genre = data["genre"]
        self._validate_fields()

    def _validate_field(self, value, expected_type, error_message, min_length=None):
        """Универсальный метод для валидации полей"""
        if not isinstance(value, expected_type):
            raise ValueError(error_message)
        if min_length and len(value) < min_length:
            raise ValueError(error_message)

    def _validate_isbn(self, isbn):
        """Проверка ISBN на соответствие формату"""
        if not re.match(r"^\d{13}$", isbn):
            raise ValueError("ISBN must be a 13-digit number.")

    def _validate_fields(self):
        """Валидация всех полей с использованием универсального метода"""
        self._validate_field(self._book_id, int, "Book ID must be a valid integer.")
        self._validate_field(self._title, str, "Title must be at least 3 characters long.", min_length=3)
        self._validate_field(self._author, str, "Author must be at least 3 characters long.", min_length=3)
        self._validate_field(self._isbn, str, "ISBN must be a string.")
        self._validate_isbn(self._isbn)

    def brief_version(self):
        return f"{self._title} by {self._author}, {self._year}"

    def full_version(self):
        return str(self)

    def __str__(self):
        return f"Book(ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Year: {self._year}, ISBN: {self._isbn}, Genre: {self._genre})"

# Перегрузка конструктора для обработки JSON или строки
class Reader:
    def __init__(self, reader_id=None, name=None, address=None, phone=None, data=None):
        if data:
            self._from_json(data)
        else:
            self._reader_id = reader_id
            self._name = name
            self._address = address
            self._phone = phone
            self._validate_fields()

    def _from_json(self, data):
        data = json.loads(data)
        self._reader_id = data["reader_id"]
        self._name = data["name"]
        self._address = data["address"]
        self._phone = data["phone"]
        self._validate_fields()


    def _validate_field(self, value, expected_type, error_message, min_length=None):
        """Универсальный метод для валидации полей"""
        if not isinstance(value, expected_type):
            raise ValueError(error_message)
        if min_length and len(value) < min_length:
            raise ValueError(error_message)

    def _validate_phone(self, phone):
        """Проверка формата телефона"""
        if not re.match(r"^\+?[0-9]{10,15}$", phone):
            raise ValueError("Phone number must be in a valid format.")

    def _validate_fields(self):
        """Валидация всех полей с использованием универсального метода"""
        self._validate_field(self._reader_id, int, "Reader ID must be a valid integer.")
        self._validate_field(self._name, str, "Name must be at least 3 characters long.", min_length=3)
        self._validate_field(self._address, str, "Address must be at least 5 characters long.", min_length=5)
        self._validate_phone(self._phone)

    def brief_version(self):
        return f"Reader: {self._name} ({self._reader_id})"

    def full_version(self):
        return str(self)

    def __str__(self):
        return f"Reader(ID: {self._reader_id}, Name: {self._name}, Address: {self._address}, Phone: {self._phone})"

    def __eq__(self, other):
        if isinstance(other, Reader):
            return self._reader_id == other._reader_id
        return False

# Класс Borrow (Запись о выдаче книги)
class Borrow(Book, Reader):
    def __init__(self, borrow_id, book_data, reader_data, date_borrowed, date_returned):
        Book.__init__(self, **book_data)  # Передаем данные о книге
        Reader.__init__(self, **reader_data)  # Передаем данные о читателе
        self._borrow_id = borrow_id
        self._date_borrowed = date_borrowed
        self._date_returned = date_returned

    def __str__(self):
        return f"Borrow(ID: {self._borrow_id}, Book: {self._book_id}, Reader: {self._reader_id}, Date Borrowed: {self._date_borrowed}, Date Returned: {self._date_returned})"

