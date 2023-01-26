from typing import Optional


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# DONE написать класс Book
class Book:

    def __init__(self, id_: Optional[int] = None, name: str = "", pages: Optional[int] = None):
        """
        Конструктор книги
        :param id_: идентификатор
        :param name: наименование
        :param pages: количество страниц
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Информация о книге
        :return: строка формата 'Книга "наименование книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, по которой можно инициализировать экземпляр класса
        :return: строка формата <class_name>(id_=<book-id>, name='<book-name>', pages=<pages-count>)
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"

# DONE написать класс Library
class Library:

    def __init__(self, books: Optional[Book] = None):
        if books is not None:
            self.books = books
        else:
            self.books = []

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            last_book = self.books[len(self.books) - 1]
            return last_book.id_ + 1

    def get_index_by_book_id(self, id_: Optional[int] = None):
        index = 0
        for book in self.books:
            if book.id_ == id_:
                return index
            index += 1
        else:
            raise ValueError


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
