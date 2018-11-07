# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal...

```python
from graphTheory.BFS.bfs import BFS
from graphTheory.Dijkstra.dijkstra import Dijkstra
from graphTheory.Graph.graph import Graph

##########
#TEST BFS
##########
print()
print("BFS traversal")
print()
gr_bfs = Graph()
gr_bfs.build_graph("graphTheory/Tests/test_graph.txt")
my_graph_bfs = gr_bfs.node_map
bfs = BFS()
bfs.graph_traversal("1", my_graph_bfs)
###############
# TEST DIJKSTRA
###############
print()
print("DIJKSTRA shortest path")
print()
gr_dj = Graph()
gr_dj.build_graph("graphTheory/Tests/test_graph.txt")
my_graph_dj = gr_dj.node_map
dijkstra = Dijkstra()
dijkstra.shortest_path("1", my_graph_dj)
node_destination = gr_dj.get_node("6")
gr_dj.print_shortest_path(node_destination)
```
