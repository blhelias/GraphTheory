### TODO

* Kruskal


# GraphTheory
Let's dive into graph theory world, we address topic such as data structures, shortest path, graph traversal, minimum spanning tree...

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
bfs.graph_traversal(1, my_graph.node_map)
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
bfs.graph_traversal(1, my_graph.node_map)
```
```
  { id: 1, num_neighbors: 3, dist: inf }
  { id: 2, num_neighbors: 1, dist: inf }
  { id: 4, num_neighbors: 1, dist: inf }
  { id: 3, num_neighbors: 1, dist: inf }
  { id: 5, num_neighbors: 1, dist: inf }
  { id: 6, num_neighbors: 0, dist: inf }
```

## Dijkstra

```python

my_graph.reset()
dijkstra = Dijkstra()
dijkstra.shortest_path(1,  my_graph.node_map)
node_destination = my_graph.get_node("6")
my_graph.print_shortest_path(node_destination)
```
```
  { id: 6, num_neighbors: 0, dist: 1.2 }
  { id: 5, num_neighbors: 1, dist: 0.5 }
  { id: 3, num_neighbors: 1, dist: 0.4 }
  { id: 4, num_neighbors: 1, dist: 0.3 }
  { id: 2, num_neighbors: 1, dist: 0.2 }
  { id: 1, num_neighbors: 3, dist: 0.0 }
```

## A* search
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

```python

my_graph.reset()
astar = Astar()
my_graph = build_graph_coor(<file_path>)
astar.shortest_path(1, 14, my_graph.node_map)
my_graph.print_shortest_path(node_destination)
```
```
{ id: 14, num_neighbors: 0, scratch: True, dist: 5.0 }
{ id: 11, num_neighbors: 3, scratch: True, dist: 4.0 }
{ id: 8, num_neighbors: 2, scratch: True, dist: 3.0 }
{ id: 4, num_neighbors: 1, scratch: True, dist: 1.0 }
{ id: 1, num_neighbors: 3, scratch: True, dist: 0.0 }

```

## Prim

<div>
  <table>
    <tr>
      <th>Graph</th>
      <th>minimum spanning tree</th>
    </tr>
    <tr>
      <td>
          <img src="https://i.imgur.com/fqaFZgP.png" width=400/>
      </td>
      <td>
          <img src="https://i.imgur.com/9kPF2UX.png" width=400/>
      </td>
    </tr>
  </table>  
</div>

```python

my_graph.reset()
prim = Prim()
my_graph = build_graph(<file_path>)
prim.minimum_spanning_tree(1, my_graph.node_map)
```
```python
{ node: 1, previous: None}
{ node: 2, previous: 1 }
{ node: 3, previous: 4 }
{ node: 4, previous: 1 }
{ node: 5, previous: 7 }
{ node: 6, previous: 7 }
{ node: 7, previous: 4 }
```



