from graph import Node, Graph
import pandas as pd


def get_data_frame(file_path: str):
    return pd.read_csv(file_path)


def fill_graph(file_path: str) -> Graph:
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


graph = fill_graph('hackathon_sirius_data.csv')

graph.display()

