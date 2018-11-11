# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal...

<div>
  <table>
    <tr>
      <th>Graph</th>
      <th>.txt file</th>
    </tr>
    <tr>
      <td>
          <img src="https://github.com/blhelias/GraphTheory/blob/master/doc/graph.PNG" width=400/>
      </td>
      <td>
        <p>1 2 0.2<br/>1 3 0.6<br/>2 4 0.1<br/>1 5 2.5<br/>3 5 0.1<br/>5 6 0.7<br/>4 3 0.1<br/></p>
      </td>
    </tr>
  </table>  
</div>

### Import

```python
from graphTheory.BFS import BFS
from graphTheory.Dijkstra import Dijkstra
from graphTheory.Graph import Graph
```
## Graph

```python
my_graph = Graph()
my_graph.build_graph(<"file path">)
```

## BFS

```python
my_graph.reset()
bfs = BFS()
bfs.graph_traversal("1", my_graph.node_map)
```
```
  { id: 1, num_neighbors: 3, dist: inf }
  { id: 2, num_neighbors: 1, dist: inf }
  { id: 3, num_neighbors: 1, dist: inf }
  { id: 5, num_neighbors: 1, dist: inf }
  { id: 4, num_neighbors: 1, dist: inf }
  { id: 6, num_neighbors: 0, dist: inf }
```

## DFS

```python
##########
#TEST BFS
##########

my_graph.reset()
bfs = BFS()
bfs.graph_traversal("1", my_graph.node_map)
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
my_graph.reset()
dijkstra = Dijkstra()
dijkstra.shortest_path("1",  my_graph.node_map)
node_destination = my_graph.get_node("6")
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
