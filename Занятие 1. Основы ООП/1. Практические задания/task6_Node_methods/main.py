from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        # добавить атрибуты
        self.value = value
        self.next_ = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self.next_})"

    def __str__(self) -> str:
        return str(self.value)

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        # вернуть значение узла
        return self.value

    # добавить метод get_next
    def get_next(self):
        return self.next_


if __name__ == '__main__':
    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел

    # с помощью метода распечатать значение первого узла
    print(first_node.get_value())
    print(first_node.get_next())
    # с помощью метода распечатать следующий узел второго узла
    print(second_node.get_value())
    print(second_node.get_next())
