from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.new_node: Optional[Node] = None

        # DONE инициализировать связный список
        if data is not None:
            for value in data:
                self.append(value)
        else:
            raise ValueError("отсутствуют исходные данные")

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value
        # return node

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __len__(self):
        return self.len

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        # DONE реализовать алгоритм добавления узла в конец последовательности
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.new_node = Node(value)
            self.linked_nodes(self.tail, self.new_node)
            self.tail = self.new_node
        self.len += 1


if __name__ == "__main__":
    list_ = [1, 2, 3]

    ll = LinkedList(list_)
    print(ll)
    # print(len(ll))

    ll.append(100)
    print(ll)
    # print(len(ll))
