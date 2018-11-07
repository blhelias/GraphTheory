# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal...
----------------------------------------
  Table                    .txt file
 ----------------------   --------------
 <img src="graph.png"/>                           
                            1 2 0.2
                            1 3 0.6
                            1 3 0.6
                            2 4 0.1
                            1 5 2.5
                            3 5 0.1
                            5 6 0.7
                            4 3 0.1
                            
-----------------------------------------
### Import

```python
from graphTheory.BFS import BFS
from graphTheory.Dijkstra import Dijkstra
from graphTheory.Graph import Graph
```

## BFS

```python
##########
#TEST BFS
##########

gr_bfs = Graph()
gr_bfs.build_graph(<"file path">)
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

## Dijkstra

```python
###############
# TEST DIJKSTRA
###############

gr_dj = Graph()
gr_dj.build_graph(<"file path">)
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
