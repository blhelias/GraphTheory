# from __future__ import annotations

class Edge:
    def __init__(self, destination, weight: float):
        self.destination: "Node" = destination
        self.weight = float(weight)
    
    def __repr__(self):
        return f" --> {self.destination.id},"\
               f" neighbors = {len(self.destination.adj_list)}"\
               f" weight : {self.weight}"