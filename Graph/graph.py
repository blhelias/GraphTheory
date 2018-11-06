
from __future__ import annotations
from typing import List, Dict

from Graph.node import Node
from Graph.edge import Edge


class Graph:
    def __init__(self) -> None:
        self.node_map: Dict = {}

    def get_node(self, node_id: int) -> Node:
        if node_id not in self.node_map:
            v = Node(node_id)
            self.node_map[node_id] = v
        else:
            v = self.node_map[node_id]
        return v

    def add_edge(self, source_node: Node, dest_node: Node, cost: float) -> None:
        v: Node = self.get_node(source_node.id)
        w: Node = self.get_node(dest_node.id)
        v.adj_list.append(Edge(w, cost))

    def build_graph(self, path: str) -> None:
        with open(path) as graph:
            graph = graph.read()
            graph = graph.split('\n')
            graph = [line.split(" ") for line in graph]

        for node_element in graph:
            v = self.get_node(node_element[0])
            w = self.get_node(node_element[1])
            self.add_edge(v, w, node_element[2])

    def __repr__(self):
        to_print = ""
        for node_key, node_value in self.node_map.items():
            to_print += f"'\n' node key = {node_key}, node value = {node_value}"
        return to_print