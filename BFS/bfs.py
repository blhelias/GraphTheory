from typing import Dict

import queue # put and get method

from ..Graph.graph import Graph

class BFS:
    """Let's implement Breadth first search algorithm
    complexity :  O(|E|+|V|)
    Example
    -------
    >>> from graphTheory.BFS import BFS
    >>> from graphTheory.Graph import Graph
    >>> gr = Graph()
    >>> gr.build_graph("test/test_graph.txt")
    >>> my_graph = gr.node_map
    >>> bfs = BFS()
    >>> bfs.graph_traversal("1", my_graph)
    { id: 1, num_neighbors: 3, dist: inf }
    { id: 2, num_neighbors: 1, dist: inf }
    { id: 3, num_neighbors: 1, dist: inf }
    { id: 5, num_neighbors: 1, dist: inf }
    { id: 4, num_neighbors: 1, dist: inf }
    { id: 6, num_neighbors: 0, dist: inf }
    """
    
    def graph_traversal(self, source: "Node", node_map: Dict):
        """Breadth first search travesal
        
        Arguments:
            source {Node} 
            node_map {Dict}
        """

        q = queue.Queue(maxsize=20)
        # Take the source node and push it int the pq
        source = node_map[source]
        # source.dist = 0.
        q.put(source)
        source.scratch = True
        node_seen = 0
        while (not q.empty()) and (node_seen < len(node_map)):
            v = q.get()
            node_seen += 1
            print(v)
            # Check each of the neighbors
            for e in v.adj_list:
                w = e.destination
                if not w.scratch:
                    q.put(w)
                    w.scratch = True