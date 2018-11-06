from __future__ import annotations
from typing import List

class Node:
    def __init__(self, id: int):
        self.id = id
        self.scratch = False
        self.adj_list: List["Edge"] = []
        self.dist = float("Inf")
    
    def __eq__(self, other: Node):
        return self.id == other.id

    def __repr__(self):
        return "{ " + f"id : {self.id}, " + f"{len(self.adj_list)}"+ " }"