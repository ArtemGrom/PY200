from collections.abc import MutableSequence
from typing import Any, Iterable, Optional
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    """Класс, описывающий односвязный список"""

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка"""
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

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
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def _to_list(self) -> list:
        """Метод для представление списка в квадратных скобках"""
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        """Метод возвращает строковое представление объекта как экземпляра"""
        return f"{self.__class__.__name__}({self._to_list()})"

    def __str__(self) -> str:
        """Метод возвращает строковое представление объекта"""
        return f"{self._to_list()}"

    def is_valid(self, index: int):
        """Проверяет объект на соответствие данным и на выход за границы индекса"""
        if not isinstance(index, int):
            raise TypeError

        if not 0 <= index < self.len:
            raise IndexError

    def __delitem__(self, key):
        """Метод реализующий удаление данных из объекта"""
        self.is_valid(key)

        if key == 0:
            self.head = self.head.next
        elif key == self.len - 1:
            node = self.step_by_step_on_nodes(self.len - 2)
            node.next = None
        else:
            prev_node = self.step_by_step_on_nodes(key - 1)
            next_node = self.step_by_step_on_nodes(key + 1)
            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def __len__(self):
        """Возвращает длину объекта"""
        return self.len

    def insert(self, index: int, value) -> None:
        """Метод для вставки значение по индексу"""
        if not isinstance(index, int):
            raise TypeError

        insert_node = Node(value)
        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len:
            self.append(value)
        elif 0 < index < self.len:
            prev_index = index - 1
            prev_node = self.step_by_step_on_nodes(prev_index)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)
            self.len += 1

    def clear(self):
        while self.len > 0:
            self.__delitem__(self.len - 1)


class DoubleLinkedList(LinkedList):
    ...


def test_linked_list():
    list_ = []
    ll = LinkedList(list_)
    print(ll)
    ll.append(1)
    ll.append("str")
    ll.append([1.1, 1.2])
    print(ll)
    print(ll.head)
    print(ll.tail)
    print(repr(ll))
    print(str(ll))
    print(len(ll))
    ll.insert(0, 5)
    print(ll)
    ll.insert(2, 7)
    print(ll)
    ll.insert(4, 10)
    print(ll)
    del ll[0]
    print(ll)
    del ll[3]
    print(ll)
    del ll[len(ll) - 1]
    print(ll)
    ll.clear()
    print(ll)


if __name__ == "__main__":
    test_linked_list()
