from __future__ import annotations
from typing import List, Dict

from ..Graph.node import Node
from ..Graph.edge import Edge


class Graph:
    """Let's build our graph !!!
    """

    def __init__(self) -> None:
        self.node_map: Dict = {} #hashmap equivalent in python

    def get_node(self, node_id: int) -> "Node":
        """ Assert a node exists. If it is not the case,
        insert it in the hashmap (dict)

        Arguments:
            node_id {int} -- key of the node we are looking for.
        
        Returns:
            Node
        """
        if node_id not in self.node_map:
            v = Node(node_id)
            self.node_map[node_id] = v
        else:
            v = self.node_map[node_id]
        return v

    def add_edge(self, source_node: Node, 
                 dest_node: Node, cost: float) -> None:
        """ Add a new neighbor for a given node
        
        Arguments:
            source_node {Node} -- node which is given new neighbor
            dest_node {Node} -- new neighbor
            cost {float} -- weight of the edge
        
        Returns:
            None 
        """
        v: Node = self.get_node(source_node.id)
        w: Node = self.get_node(dest_node.id)
        v.adj_list.append(Edge(w, cost))

    def build_graph(self, path: str) -> None:
        """Build graph, which is a map of nodes
        
        Arguments:
            path {str} -- path of the .txt file representing the graph
        
        Returns:
            None
        """
        with open(path) as graph:
            graph = graph.read()
            graph = graph.split('\n')
            graph = [line.split(" ") for line in graph]

        for node_element in graph:
            v = self.get_node(node_element[0])
            w = self.get_node(node_element[1])
            self.add_edge(v, w, node_element[2])
    
    def print_shortest_path(self, destination_node: "Node"):
        dist: float = destination_node.dist
        path_node = destination_node
        print(path_node)
        while dist > 0.:
            path_node = path_node.prev
            dist = path_node.dist
            print(path_node)

    def __repr__(self) -> None:
        """Print our graph
        """
        to_print = ""
        for node_key, node_value in self.node_map.items():
            to_print += f"'\n' node key = {node_key}, node value = {node_value}"
        return to_print
