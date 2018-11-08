from ..Graph.node import Node
from ..Graph.edge import Edge
from ..Graph.graph import Graph
from ..Graph.path import Path
from ..utils import PriorityQueue
from ..Dijkstra.dijkstra import Dijkstra
from ..BFS.bfs import BFS
from ..DFS.dfs import DFS
import random

"""Ugly testing script
"""

def test_node():
    node_1 = Node(1)
    node_2 = Node(1)
    node_3 = Node(2)
    node_4 = Node(int(1.0))
    assert node_1 == node_2 and not (node_1 == node_3)
    assert node_1 == node_4

def test_get_node():
    node_map = {1: Node(1), 2: Node(2)}
    gr = Graph()
    gr.node_map = node_map
    gr.get_node(3)
    assert gr.node_map == {1: Node(1), 2: Node(2), 3: Node(3)}

def test_add_edge():
    n = Node(0)
    gr = Graph()
    n = gr.get_node(n.id)
    gr.add_edge(n, Node(3), 0.7)
    gr.add_edge(n, Node(2), 0.7)
    gr.add_edge(n, Node(1), 0.7)
    print(n.adj_list) # print the results and see what happens

def test_build_graph():
    gr = Graph()
    gr.build_graph("Tests/test_graph.txt")
    print(gr) # only print the graph to check results

def test_path():
    p1 = Path(Node(0), 0.6)
    p2 = Path(Node(0), 0.5)
    assert p1 > p2

def  test_priority_q():
    pq = PriorityQueue()
    gr = Graph()
    gr.build_graph("Tests/test_graph.txt")
    random.seed(777)
    for _, value in gr.node_map.items():
        value.dist = random.random()
        pq.push(Path(value, value.dist))
    res = []
    while len(pq._queue)>0:
        node_out = pq.pop()
        res.append(int(node_out.id))
    assert res == [1, 4, 5, 3, 2, 6]

def test_print_shotest_path():
    gr = Graph()
    gr.build_graph("Tests/test_graph.txt")
    my_graph = gr.node_map
    dijkstra = Dijkstra()
    dijkstra.shortest_path("1", my_graph)
    print()
    print("Dijkstra")
    print()
    node_destination = gr.get_node("6")
    gr.print_shortest_path(node_destination)

def test_bfs():
    gr = Graph()
    gr.build_graph("Tests/test_graph.txt")
    my_graph = gr.node_map
    bfs = BFS()
    print()
    print("BFS")
    print()
    bfs.graph_traversal("1", my_graph)

def test_dfs_rec():
    graph_dfs = Graph()
    graph_dfs.build_graph("Tests/test_graph.txt")
    my_graph_dfs = graph_dfs.node_map
    dfs = DFS()
    print()
    print("DFS recursive")
    print()
    dfs.graph_traversal_rec("1", my_graph_dfs)

def test_dfs():
    graph_dfs = Graph()
    graph_dfs.build_graph("Tests/test_graph.txt")
    my_graph_dfs = graph_dfs.node_map
    dfs = DFS()
    print()
    print("DFS iterative")
    print()
    dfs.graph_traversal("1", my_graph_dfs)

def test_reset():
    graph_dfs = Graph()
    graph_dfs.build_graph("Tests/test_graph.txt")
    my_graph_dfs = graph_dfs.node_map
    dfs = DFS()
    print()
    print("DFS iterative")
    print()
    dfs.graph_traversal("1", my_graph_dfs)
    print()
    print(my_graph_dfs)
    graph_dfs.reset()
    print(my_graph_dfs)