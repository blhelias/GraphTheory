# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal...

<div>
  <table>
    <tr>
      <th>Graph</th>
      <th>node1 node2 weight</th>
    </tr>
    <tr>
      <td>
          <img src="https://i.imgur.com/zo5qdaX.png" width=400/>
      </td>
      <td>
          <img src="https://i.imgur.com/VlIlALP.png" width=200/>
      </td>
    </tr>
  </table>  
</div>

### Import

```python
from graphTheory.Graph import Graph
from graphTheory.BFS import BFS
from graphTheory.DFS import DFS
from graphTheory.Dijkstra import Dijkstra
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

# TODO: Astar
<div>
  <table>
    <tr>
      <th>Graph</th>
      <th>node1 node2 weight x1 y1 x2 y2</th>
    </tr>
    <tr>
      <td>
          <img src="https://i.imgur.com/sKyagB6.png" width=400/>
      </td>
      <td>
          <img src="https://i.imgur.com/v5VTtKn.png" width=250/>
      </td>
    </tr>
  </table>  
</div>
