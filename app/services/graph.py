class Node:
    def __init__(self, start: int, max_train_tonage: float = 0) -> None:
        """
        Создает новый узел графа.

        :param start: Начальная точка узла.
        :param end: Конечная точка узла.
        :param tonnage_limit: Лимит по тоннажу.
        :param max_train_tonage: Максимальный тоннаж поезда.
        """
        self.start = start
        self.quantity_limit = 0
        # tonnage_limits - это словарь словарей - где ключ это id(start) и
        # для предыдущего значения  ( на примере на листочке для буквы С tonnage_limits будет хранится в букве А )
        # а значение - это словарь в котором 2 ключа длина пути(lenght), tonnage_limit - а значения их числовой эквивалент
        self.tonnage_limits = {}
        self.max_train_tonnage = max_train_tonage
        self.next: list[Node] = []


class Graph:
    def __init__(self) -> None:
        """Создает пустой граф."""
        # ключ - это старт ноды, значение - сама нода
        self.nodes: dict[str, Node] = {}

    def add_node(self, node: Node) -> Node:
        """
        Добавляет новый узел в граф.

        :param node: Объект Node, представляющий узел графа.
        :return: Добавленный узел.
        """
        self.nodes[node.start] = node

    def add_edge(self, node1: Node, node2: Node) -> None:
        """
        Создает ребро между двумя узлами.

        :param node1: Первый узел.
        :param node2: Второй узел.
        :param path_length: Длина пути между узлами.
        """
        node1.next.append(node2)

    def display(self) -> None:
        """Отображает связи между узлами в графе."""
        for node in self.nodes.values():
            connected_nodes = [f"Узел {n.start}" for n in node.next]
            print(
                f"Узел {node.start} соединён с: {', '.join(connected_nodes)} и имеет пропускную способность {node.quantity_limit}"
            )
    def find_all_quantity(self, start_node: Node) -> list[float]:
        """
        Находит пропускную способность для всех узлов, начиная с указанного узла.

        :param start_node: Начальный узел, с которого начинается поиск пропускной способности.
        :return: Список пропускных способностей для всех узлов, доступных из начального узла.
        :rtype: list[float]
        """
        quantities = []
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            quantities.append(current_node.quantity_limit)

            for next_node in current_node.next:
                stack.append(next_node)

        return quantities

