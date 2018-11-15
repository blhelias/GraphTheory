from typing import Dict

import math

from ..Graph import Graph
from ..Graph import Path
from ..utils import PriorityQueue


class Astar:
    """Let's implement A* algorithm !
    A * start algorithm is similar to dijkstra, and introduces the
    notion of heuristic to make the smarter decision at each node.
    We could say that dijkstra is a special case of A* where
    the heuristic score is equal to 0.
    Complexity : O(|E|) worst case

    Example
    -------
        >>> from ..Graph import Graph
        >>> from ..A_star import Astar
        >>> gr = Graph()
        >>> gr.build_graph("../test/test_graph_coor.txt")
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

    def shortest_path(self, source: int, end: int, node_map: Dict):
        pq = PriorityQueue()
        # Initialize distance and visited parameter for each node
        for _, value_node in node_map.items():
            value_node.scratch = False
            value_node.det_dist = float("Inf")
        # Take the source node and push it int the pq
        source = node_map[source]
        source.dist = 0.
        end = node_map[end]
        priority = self.heuristic(source, end) + source.dist
        pq.push(Path(source, priority))
        # Begin dijkstra shortest path !
        node_seen = 0
        while not(end.scratch):
            v = pq.pop() # path.dest
            print(v)
            # Check if we already visited the node
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
                h_w = self.heuristic(w, end)
                # update distance of the node if necessary
                if w.dist >= v.dist + cost_vw:
                    w.dist = v.dist + cost_vw
                    w.prev = v
                    pq.push(Path(w, w.dist + h_w))

    def heuristic(self, v, end):
        coor_v = v.coor
        coor_end = end.coor
        return self.d_euclidian(coor_v, coor_end)

    def d_euclidian(self, coor1, coor2):
        sub_x = (coor1[0] - coor2[0]) ** 2
        sub_y = (coor1[1] - coor2[1]) ** 2
        return math.sqrt(sub_x + sub_y)
