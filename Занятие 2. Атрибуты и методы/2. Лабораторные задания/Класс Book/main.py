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

    def __init__(self, id_: int = 0, name: str = "", pages: int = 0):
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
