# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal...

```python
from graphTheory.BFS.bfs import BFS
from graphTheory.Dijkstra.dijkstra import Dijkstra
from graphTheory.Graph.graph import Graph

##########
#TEST BFS
##########

gr_bfs = Graph()
gr_bfs.build_graph("graphTheory/Tests/test_graph.txt")
my_graph_bfs = gr_bfs.node_map
bfs = BFS()
bfs.graph_traversal("1", my_graph_bfs)
```
```
  { id: 1, num_neighbors: 3, dist: inf }
  { id: 2, num_neighbors: 1, dist: inf }
  { id: 3, num_neighbors: 1, dist: inf }
  { id: 5, num_neighbors: 1, dist: inf }
  { id: 4, num_neighbors: 1, dist: inf }
  { id: 6, num_neighbors: 0, dist: inf }
```

```python
###############
# TEST DIJKSTRA
###############

gr_dj = Graph()
gr_dj.build_graph("graphTheory/Tests/test_graph.txt")
my_graph_dj = gr_dj.node_map
dijkstra = Dijkstra()
dijkstra.shortest_path("1", my_graph_dj)
node_destination = gr_dj.get_node("6")
gr_dj.print_shortest_path(node_destination)
```
```
  { id: 6, num_neighbors: 0, dist: 1.2 }
  { id: 5, num_neighbors: 1, dist: 0.5 }
  { id: 3, num_neighbors: 1, dist: 0.4 }
  { id: 4, num_neighbors: 1, dist: 0.3 }
  { id: 2, num_neighbors: 1, dist: 0.2 }
  { id: 1, num_neighbors: 3, dist: 0.0 }
```
