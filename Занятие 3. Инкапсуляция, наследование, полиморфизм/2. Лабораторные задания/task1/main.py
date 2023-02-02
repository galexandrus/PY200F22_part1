from typing import Union


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.check_name(name)
        self.check_author(author)
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}, Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.check_name(new_name)
        self.__name = new_name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, new_author: str) -> None:
        self.check_author(new_author)
        self.__author = new_author

    @staticmethod
    def check_name(name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("название книги должно быть типа str")
        if name == "":
            raise ValueError("название книги не может быть пустой строкой")

    @staticmethod
    def check_author(author: str) -> None:
        if not isinstance(author, str):
            raise TypeError("имя автора должно быть типа str")
        if author == "":
            raise ValueError("имя автора не может быть пустой строкой")

    @staticmethod
    def check_pages(value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("количество страниц должно быть целым числом")
        elif value <= 0:
            raise ValueError("количество страниц не может быть отрицательным")


    @staticmethod
    def check_duration(value: Union[int, float]) -> None:
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("длительность должна быть типа float или int")
        elif value <= 0:
            raise ValueError("длительность не может быть отрицательной")


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.check_pages(pages)
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.check_duration(duration)
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    paper_book = PaperBook("Приключения мартышки", "Обезьянка Чичи", 234)
    audio_book = AudioBook("Как играть в боулинг", "Лебовски", 23.5)
    print(paper_book)
    print(audio_book)
