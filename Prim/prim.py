from typing import Dict

from ..Graph import Graph
from ..Graph import Path
from ..utils import PriorityQueue


class Prim:
    def __init__(self):
        self.edge_list = []

    def minimum_spanning_tree(self, source: int, node_map: Dict):
        pq = PriorityQueue()
        # Take the source node and push it int the pq
        source = node_map[source]
        source.dist = 0.
        pq.push(Path(source, source.dist))
        # Begin dijkstra shortest path !
        while (not pq.is_empty()):
            v = pq.pop() # Path.dest
            # Check if we already visited the node
            if v.scratch:
                continue # Make new iteration
            v.scratch = True # Now it's visited
            # Check each neighbors
            for e in v.adj_list:
                w = e.destination
                print(w)
                cost_vw = e.weight
                # Check if weights are positives
                if cost_vw < 0:
                    raise ValueError(" Graph has negative weight !!!")
                # update distance of the node if necessary
                if w.dist > cost_vw and not w.scratch: # Make sure the node 
                # hasn't been discovered visited otherwise it will cause some issues.     
                    w.dist = cost_vw
                    w.prev = v
                    pq.push(Path(w, w.dist))

        for _, value_node  in node_map.items():
            rep = ""
            rep = "{ node: " + str(value_node.id) + ", previous: "
            if value_node.prev is not None:
                rep += str(value_node.prev.id) + " }"
            print(rep)
