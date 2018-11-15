from typing import Dict

import queue # put and get method

from ..Graph.graph import Graph

class DFS:
    """Let's implement Breadth first search algorithm
    complexity :  O(|E|+|V|)
    Example
    -------
    >>> from graphTheory.DFS import DFS
    >>> from graphTheory.Graph import Graph
    >>> gr = Graph()
    >>> gr.build_graph("test/test_graph.txt")
    >>> my_graph = gr.node_map
    >>> dfs = DFS()
    >>> dfs.graph_traversal("1", my_graph)
    { id: 1, num_neighbors: 3, dist: inf }
    { id: 2, num_neighbors: 1, dist: inf }
    { id: 4, num_neighbors: 1, dist: inf }
    { id: 3, num_neighbors: 1, dist: inf }
    { id: 5, num_neighbors: 1, dist: inf }
    { id: 6, num_neighbors: 0, dist: inf }

    WARNING: These 2 variations of DFS (recursion ant iteration)
    visit each vertex in the opposite order from each other
    in our example first recursive technic gives {1, 2, 4, 3, 5, 6}
    whereas the 2nd iterative technic gives us {1, 5, 6, 3, 2, 4}
    """

    def graph_traversal_rec(self, source: "Node", node_map: Dict):
        """Depth-first search travesal in a recursive way
        Visit child vertices before sibblings (lexicographic order)

        Arguments:
            source {Node}
            node_map {Dict}
        """
        source = node_map[source]
        source.scratch = True
        print(source)
        for e in source.adj_list:
            if not e.destination.scratch:
                self.graph_traversal_rec(str(e.destination.id), node_map)

    def graph_traversal(self, source: "Node", node_map: Dict):
        """Depth-first search travesal in an iterative way
        Visit child vertices before sibblings (lexicographic order)

        Arguments:
            source {Node}
            node_map {Dict}
        """

        stack = []
        # Take the source node and push it int the pq
        source = node_map[source]
        # source.dist = 0.
        stack.append(source)
        source.scratch = True
        node_seen = 0
        while len(stack) != 0 and (node_seen < len(node_map)):
            v = stack.pop()
            node_seen += 1
            print(v)
            # Check each of the neighbors
            for e in v.adj_list:
                w = e.destination
                if not w.scratch:
                    stack.append(w)
                    w.scratch = True
