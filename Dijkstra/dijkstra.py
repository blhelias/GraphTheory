from typing import Dict
import sys
sys.path.insert(0, "../")
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
            for _, e in enumerate(v.adj_list):
                w = e.destination
                cost_vw = e.weight
                # Check weights are positives
                if cost_vw < 0:
                    raise ValueError(" Graph has negative weight !!!")
                # update distance of the node if necessary
                if w.dist > (v.dist + cost_vw):
                    w.dist = v.dist + cost_vw
                    w.prev = v
                    pq.push(Path(w, w.dist))

if __name__ == "__main__":
    gr = Graph()
    gr.build_graph("../test/test_graph.txt")
    my_graph = gr.node_map
    dijkstra = Dijkstra()
    dijkstra.shortest_path("1", my_graph)