# from __future__ import annotations
from typing import List

class Node:
    def __init__(self, id: int) -> None:
        self.id = id
        self.scratch = False
        self.adj_list: List["Edge"] = []
        self.dist = float("Inf")
        self.prev = None
        self.coor = None

    def set_coor(self, tuple_coor):
        if self.coor == None:
            self.coor = tuple_coor

    def __eq__(self, other: "Node"):
        return self.id == other.id

    def __repr__(self):
        return "{ " + f"id: {self.id}, "\
                + f"num_neighbors: {len(self.adj_list)}, "\
                + f"scratch: {self.scratch}, "\
                + f"dist: {self.dist}"\
                + " }"
