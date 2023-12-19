"""Graph generation utilities."""
import networkx as nx

from .adt import AppConfig, Graph
from .graphics import print_adjacency_matrix, to_html


def generate_graph(num_nodes: int, network_type: str) -> Graph:
    """Generates a graph of a given type with the specified number of nodes.

    :param num_nodes: number of nodes to generate.
    :type num_nodes: int
    :param network_type: type of network to generate
    :type network_type: str
    :raises ValueError: if the network type is not supported
    :return: a graph with the specified characteristics.
    :rtype: Graph
    """
    if network_type == "barabasi-albert":
        return nx.barabasi_albert_graph(n=num_nodes, m=int(num_nodes / 3))
    if network_type == "complete":
        return nx.complete_graph(n=num_nodes)
    if network_type == "erdos-renyi":
        return nx.erdos_renyi_graph(n=num_nodes, p=0.33)
    raise ValueError(f"invalid network type '{network_type}'")


def generate_network(config: AppConfig):
    """TBD."""
    graph = generate_graph(num_nodes=config.nodes, network_type=config.network_type)
    print_adjacency_matrix(graph)
    to_html(graph)
