from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next_ = next_

    def get_value(self) -> Any:
        return self.value

    def get_next(self) -> Optional:
        return self.next_


if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)

    print(first_node.get_value())
    print(first_node.get_next())
    ...  # TODO c помощью методов распечатать значение первого узла и следующий узел второго узла
