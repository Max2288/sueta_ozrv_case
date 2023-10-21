from app.services.graph import Node, Graph
import pandas as pd


def get_data_frame(file_path: str) -> pd.DataFrame:
    """
    Чтение данных из CSV-файла и возврат их в виде объекта DataFrame.

    :param file_path: Путь к CSV-файлу, содержащему данные.
    :type file_path: str
    :return: Объект DataFrame, представляющий данные из CSV-файла.
    :rtype: pd.DataFrame
    """
    return pd.read_csv(file_path)


def fill_graph(file_path: str) -> Graph:
    """
    Заполняет граф данными из CSV-файла и возвращает граф.

    :param file_path: Путь к CSV-файлу, содержащему данные о графе.
    :type file_path: str
    :return: Граф, заполненный данными из CSV-файла.
    :rtype: Graph
    """
    graph = Graph()
    df = get_data_frame(file_path)
    for _, row in df.iterrows():
        start_value = int(row['start'])
        end_value = int(row['end'])
        length_value = float(row['length'])
        tonnage_limit_value = int(row['tonnage_limit'])
        max_train_tonnage_value = float(row['max_train_tonnage'])
        if end_value not in graph.nodes:
            end_node = Node(end_value, max_train_tonnage_value)
            graph.add_node(end_node)
        if start_value in graph.nodes:
            # проверяем по длине
            start_node: Node = graph.nodes[start_value]
            start_tonage_length = start_node.tonnage_limits.get(
                'length',
                0
            )
            if start_tonage_length == length_value:
                continue
            else:
                graph.add_edge(start_node, graph.nodes[end_value])
        else:
            node = Node(start_value, max_train_tonnage_value)
            graph.add_node(node)
            graph.add_edge(node, graph.nodes[end_value])
        end_node: Node = graph.nodes[end_value]
        end_node.tonnage_limits = {
            'length': length_value,
            'tonnage_limit': tonnage_limit_value
        }
    return graph

def generate_quantity(graph: Graph) -> Graph:
    """
    Генерирует количество для каждого узла в графе на основе ограничений на грузоподъемность.

    :param graph: Граф, для которого нужно сгенерировать количество.
    :type graph: Graph
    :return: Граф с расчитанными количествами для каждого узла.
    :rtype: Graph
    """
    for _, node in graph.nodes.items():
        quantities_for_parent_node = []
        quantities_for_child_node = []
        for child_node in node.next:
            quantity = int(child_node.tonnage_limits.get("tonnage_limit", 0) / node.max_train_tonnage)
            quantities_for_parent_node.append({child_node.start:quantity})
        if quantities_for_parent_node:
            quantities_for_parent_node = sorted(quantities_for_parent_node, key=lambda x: list(x.values())[0])
            max_child = quantities_for_parent_node[0]
            child_child_node = graph.nodes[list(max_child.keys())[0]]
            for child_node in child_child_node.next:
                quantity = int(child_node.tonnage_limits.get("tonnage_limit", 0) / child_child_node.max_train_tonnage)
                quantities_for_child_node.append({child_node.start:quantity})
            current_max = list(max_child.values())[0]
            child_sum = sum([list(value.values())[0] for value in quantities_for_child_node])
            if current_max > child_sum:
                if len(quantities_for_parent_node) > 1:
                    next_child: Node = graph.nodes[list(quantities_for_parent_node.pop().keys())[0]]
                    next_child.quantity_limit = current_max - child_sum
            child_child_node.quantity_limit = child_sum
    return graph
