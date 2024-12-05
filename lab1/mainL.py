import re  # Импортируем модуль регулярных выражений для проверки формата ISBN и телефона
import json  # Импортируем модуль для работы с JSON (парсинг и сериализация данных)

# Класс Book (Книга)
class Book:
    def __init__(self, book_id, title, author, year, isbn, genre):
        # Инициализатор класса Book, принимает все необходимые параметры для книги
        self._book_id = book_id  # Присваиваем идентификатор книги
        self._title = title  # Присваиваем название книги
        self._author = author  # Присваиваем автора книги
        self._year = year  # Присваиваем год издания книги
        self._isbn = isbn  # Присваиваем ISBN книги
        self._genre = genre  # Присваиваем жанр книги
        self._validate_fields()  # Вызываем метод валидации полей

    def _validate_field(self, value, expected_type, error_message, min_length=None):
        # Универсальный метод валидации для проверки типа и минимальной длины значения
        if not isinstance(value, expected_type):  # Проверка типа значения
            raise ValueError(error_message)  # Если тип неверный, вызываем исключение
        if min_length and len(value) < min_length:  # Проверка минимальной длины, если она указана
            raise ValueError(error_message)  # Если длина меньше минимальной, вызываем исключение

    def _validate_isbn(self, isbn):
        # Метод для проверки формата ISBN (13 цифр)
        if not re.match(r"^\d{13}$", isbn):  # Проверка на регулярное выражение: должно быть 13 цифр
            raise ValueError("ISBN must be a 13-digit number.")  # Если ISBN не соответствует формату, вызываем исключение

    def _validate_fields(self):
        # Метод для валидации всех полей книги
        self._validate_field(self._book_id, int, "Book ID must be a valid integer.")  # Валидация ID книги
        self._validate_field(self._title, str, "Title must be at least 3 characters long.", min_length=3)  # Валидация названия
        self._validate_field(self._author, str, "Author must be at least 3 characters long.", min_length=3)  # Валидация автора
        self._validate_field(self._isbn, str, "ISBN must be a string.")  # Валидация ISBN
        self._validate_isbn(self._isbn)  # Валидация формата ISBN

    def brief_version(self):
        # Метод для краткого представления книги
        return f"{self._title} by {self._author}, {self._year}"  # Возвращает строку с названием, автором и годом

    def full_version(self):
        # Метод для полного представления книги
        return str(self)  # Возвращает полную строку с деталями книги через метод __str__

    def __str__(self):
        # Метод для вывода всех данных о книге в строковом формате
        return f"Book(ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Year: {self._year}, ISBN: {self._isbn}, Genre: {self._genre})"

# Класс Reader (Читатель)
class Reader:
    def __init__(self, reader_id=None, name=None, address=None, phone=None, data=None):
        # Конструктор читателя, который либо принимает данные напрямую, либо извлекает их из JSON
        if data:
            self._from_json(data)  # Если передан параметр data, загружаем из JSON
        else:
            self._reader_id = reader_id  # Инициализируем ID читателя
            self._name = name  # Инициализируем имя читателя
            self._address = address  # Инициализируем адрес читателя
            self._phone = phone  # Инициализируем номер телефона читателя
            self._validate_fields()  # Валидация всех полей

    def _from_json(self, data):
        # Метод для извлечения данных из JSON
        data = json.loads(data)  # Преобразуем строку JSON в словарь
        self._reader_id = data["reader_id"]  # Извлекаем и присваиваем ID читателя
        self._name = data["name"]  # Извлекаем и присваиваем имя читателя
        self._address = data["address"]  # Извлекаем и присваиваем адрес читателя
        self._phone = data["phone"]  # Извлекаем и присваиваем телефон читателя
        self._validate_fields()  # Валидация всех полей после извлечения данных

    def _validate_field(self, value, expected_type, error_message, min_length=None):
        # Универсальный метод для валидации полей
        if not isinstance(value, expected_type):  # Проверка типа значения
            raise ValueError(error_message)  # Если тип неверный, вызываем исключение
        if min_length and len(value) < min_length:  # Проверка минимальной длины, если указана
            raise ValueError(error_message)  # Если длина меньше минимальной, вызываем исключение

    def _validate_phone(self, phone):
        # Метод для проверки формата телефона (10-15 цифр с возможным знаком +)
        if not re.match(r"^\+?[0-9]{10,15}$", phone):  # Проверка на регулярное выражение: правильный формат телефона
            raise ValueError("Phone number must be in a valid format.")  # Если формат неверный, вызываем исключение

    def _validate_fields(self):
        # Метод для валидации всех полей читателя
        self._validate_field(self._reader_id, int, "Reader ID must be a valid integer.")  # Валидация ID читателя
        self._validate_field(self._name, str, "Name must be at least 3 characters long.", min_length=3)  # Валидация имени
        self._validate_field(self._address, str, "Address must be at least 5 characters long.", min_length=5)  # Валидация адреса
        self._validate_phone(self._phone)  # Валидация телефона

    def brief_version(self):
        # Метод для краткого представления читателя
        return f"Reader: {self._name} ({self._reader_id})"  # Возвращает строку с именем и ID читателя

    def full_version(self):
        # Метод для полного представления читателя
        return str(self)  # Возвращает полную строку с деталями читателя через метод __str__

    def __str__(self):
        # Метод для вывода всех данных о читателе в строковом формате
        return f"Reader(ID: {self._reader_id}, Name: {self._name}, Address: {self._address}, Phone: {self._phone})"

    def __eq__(self, other):
        # Метод для сравнения двух объектов Reader по ID
        if isinstance(other, Reader):
            return self._reader_id == other._reader_id  # Возвращает True, если ID читателей одинаковы
        return False

# Класс Borrow (Запись о выдаче книги)
class Borrow(Book, Reader):
    def __init__(self, borrow_id, book_data, reader_data, date_borrowed, date_returned):
        # Конструктор записи о выдаче книги, принимает ID записи, данные книги и читателя
        Book.__init__(self, **book_data)  # Передаем данные книги в конструктор класса Book
        Reader.__init__(self, **reader_data)  # Передаем данные читателя в конструктор класса Reader
        self._borrow_id = borrow_id  # Инициализируем ID записи о выдаче
        self._date_borrowed = date_borrowed  # Инициализируем дату выдачи
        self._date_returned = date_returned  # Инициализируем дату возврата

    def __str__(self):
        # Метод для вывода всех данных о записи о выдаче
        return f"Borrow(ID: {self._borrow_id}, Book: {self._book_id}, Reader: {self._reader_id}, Date Borrowed: {self._date_borrowed}, Date Returned: {self._date_returned})"

# Класс ReaderBrief (Краткая версия читателя)
class ReaderBrief:
    def __init__(self, reader):
        # Конструктор для создания краткой версии данных читателя
        self._name = reader._name  # Сохраняем имя читателя
        self._phone = reader._phone  # Сохраняем телефон читателя

    def __str__(self):
        # Метод для представления краткой версии данных читателя
        return f"Name: {self._name}, Phone: {self._phone}"


# Пример использования классов:

# Данные для книги (в виде словаря)
book_data = {
    "book_id": 1,
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "isbn": "9780451524935",
    "genre": "Dystopian"
}

# Данные для читателя (в виде словаря)
reader_data = {
    "reader_id": 1,
    "name": "John Doe",
    "address": "123 Main St",
    "phone": "+1234567890"
}

# Создание экземпляра класса Borrow (Запись о выдаче)
borrow = Borrow(1, book_data, reader_data, "2024-12-05", "2024-12-20")

# Вывод информации о записи
print(borrow)  # Запись о выдаче
