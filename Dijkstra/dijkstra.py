"""
Example:
    >>> gr = Graph()
    >>> gr.build_graph("../test/test_graph.txt")
    >>> my_graph = gr.node_map
    >>> dijkstra = Dijkstra()
    >>> dijkstra.shortest_path("1", my_graph)
    >>> node_destination = gr.get_node("6")
    >>> gr.print_shortest_path(node_destination)
    { id: 6, num_neighbors: 0, dist: 1.2 }
    { id: 5, num_neighbors: 1, dist: 0.5 }
    { id: 3, num_neighbors: 1, dist: 0.4 }
    { id: 4, num_neighbors: 1, dist: 0.3 }
    { id: 2, num_neighbors: 1, dist: 0.2 }
    { id: 1, num_neighbors: 3, dist: 0.0 }
"""

import sys
sys.path.insert(0, "../")

from typing import Dict

from Graph.graph import Graph
from Graph.path import Path
from utils import PriorityQueue


class Dijkstra:
    """Complexity : O(|V|**2)
    """
    def shortest_path(self, source: "Node", node_map: Dict):
        pq = PriorityQueue()
        # Initialize distance and visited parameter for each node
        for _, value_node in node_map.items():
            value_node.scratch = False
            value_node.det_dist = float("Inf")
        # Take the source node and push it int the pq
        source = node_map[source]
        source.dist = 0.
        pq.push(Path(source, source.dist))
        # Begin dijkstra shortest path !
        node_seen = 0
        while (not pq.is_empty()) and (node_seen < len(node_map)):
            v = pq.pop() # path.dest
            #  Check if we already visited the node 
            if v.scratch:
                continue
            # Now it 's visited
            v.scratch = True
            node_seen += 1
            # Check each of the neighbors
            for e in v.adj_list:
                w = e.destination
                cost_vw = e.weight
                # Check if weights are positives
                if cost_vw < 0:
                    raise ValueError(" Graph has negative weight !!!")
                # update distance of the node if necessary
                if w.dist >= v.dist + cost_vw:
                    w.dist = v.dist + cost_vw
                    w.prev = v
                    pq.push(Path(w, w.dist))
