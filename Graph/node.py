from __future__ import annotations
from typing import List
from Graph.edge import Edge

class Node:
    def __init__(self, id: int):
        self.__id = id
        self.__visited = False
        self.adj_list: List[Edge] = []
        self.__dist = float("Inf")
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_visited(self):
        return self.__visited

    def set_visited(self, visited):
        self.__visited = visited
    
    def get_dist(self):
        return self.__dist

    def set_dist(self, dist):
        self.__dist = dist

    def __eq__(self, other: Node):
        return self.__id == other.get_id()

    def __repr__(self):
        return "{ " + f"id : {self.__id}, " + f"{len(self.adj_list)}"+ " }"