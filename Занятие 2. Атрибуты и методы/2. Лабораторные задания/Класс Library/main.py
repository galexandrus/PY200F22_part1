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

    def __init__(self, books: Optional[list] = None):
        """
        Конструктор библиотеки
        :param books: список книг
        """
        if books is None:
            self.books = []
        else:
            if not isinstance(books, list):
                raise TypeError("необходимо передать список книг")
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("список должен состоять из книг")
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод для получения идентификатора для добавления новой книги в библиотеку
        :return: идентификатор (атрибут экземпляра класса Book)
        """
        if len(self.books) == 0:
            return 1
        else:
            last_book = self.books[len(self.books) - 1]
            return last_book.id_ + 1

    def get_index_by_book_id(self, id_: Optional[int] = None):
        """
        Метод, возвращающий индекс книги в списке
        :param id_: id книги, индекс которой нужно найти
        :return: индекс (порядковый номер в списке книг)
        """
        for i in range(len(self.books)):
            book = self.books[i]
            if book.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"],
             name=book_dict["name"],
             pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    # print(library_with_books.get_index_by_book_id(2))

    # print(isinstance(list_books, list))
    # for book in list_books:
    #     print(isinstance(book, Book))
    #     print(f"{book.__class__.__name__}(id_={book.id_}, name='{book.name}', pages={book.pages})")
    # print(type(list_books))
    # print(type(list()))
