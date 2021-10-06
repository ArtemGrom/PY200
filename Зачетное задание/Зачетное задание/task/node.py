from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """Инициализируем узел для односвязного списка"""
        self.value = value
        self.next = next_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None):
        self.is_valid(next_)
        self._next = next_

    @classmethod
    def is_valid(cls, node: Any):
        """Проверяем на верный формат входных данных"""
        if not isinstance(node, (type(None), Node)):
            raise TypeError("Неверный формат входных данных")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self):
        if self._next is None:
            return f"Node({self.value}, {None})"
        else:
            return f"Node({self.value}, Node({self._next}))"


class DoubleLinkedNode(Node):
    """Класс, инициализирующий двусвязный список"""

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"] = None):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self):
        if self._next is None and self._prev is None:
            return f"DoubleLinkedNode({self.value}, {None}, {None})"
        elif self._next is None:
            return f"DoubleLinkedNode({self.value}, {None}, DoubleLinkedNode({self.prev}))"
        elif self._prev is None:
            return f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self._next}), {None})"
        else:
            return f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self._next}), DoubleLinkedNode({self.prev}))"


def test_double_linked_node():
    first_node = DoubleLinkedNode(1)
    second_node = DoubleLinkedNode(2)
    third_node = DoubleLinkedNode(3)
    forth_node = DoubleLinkedNode(10)

    first_node.next = second_node
    third_node.prev = second_node
    second_node.prev, second_node.next = first_node, third_node

    assert repr(first_node) == "DoubleLinkedNode(1, DoubleLinkedNode(2), None)"
    assert repr(second_node) == "DoubleLinkedNode(2, DoubleLinkedNode(3), DoubleLinkedNode(1))"
    assert repr(third_node) == "DoubleLinkedNode(3, None, DoubleLinkedNode(2))"
    assert repr(forth_node) == "DoubleLinkedNode(10, None, None)"


if __name__ == "__main__":
    test_double_linked_node()
