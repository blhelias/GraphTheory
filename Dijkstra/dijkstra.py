from typing import Dict

import heapq
import sys
# sys.path.append("../")
# print(sys.path)
from Graph.graph import Graph

class Dijkstra:
    """
    Complexity : O(|V|**2)
    """
    def __init__(self):
        self.pq = heapq.heapify([])

    def shortest_path(self, source: "Node", node_map: Dict):
        # Initialize distance and visited parameter for each node
        for _, value_node in node_map.items():
            value_node.scratch = False
            value_node.det_dist = float("Inf")

        source = node_map[source.get_id()]
        source.set_dist(0.)
        heapq.heappush(self.pq, source)
        # begin dijkstra shortest path
        node_seen = 0
        # while (len(self.pq) > 0) and (node_seen < len(node_map)):
        #     vrec: "Path" = heapq.heappop(self.pq)
        #     v = vrec.dest

if __name__ == "__main__":
    gr = Graph()
    gr.build_graph("../test/graph.txt")
    my_graph = gr.node_map
    dijkstra = Dijkstra()
    dijkstra.shortest_path(1995, my_graph)