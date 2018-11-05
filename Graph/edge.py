from __future__ import annotations

class Edge:
    def __init__(self, destination, weight: float):
        # self.node_from = node_from
        self.destination = destination
        self.weight = weight
    
    def __repr__(self):
        return f" --> {self.destination.get_id()}, neighbors\
                 = {len(self.destination.adj_list)} weight : {self.weight}"