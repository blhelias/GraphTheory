from Graph.node import Node
from Graph.edge import Edge
from Graph.graph import Graph
from Graph.path import Path
from utils import PriorityQueue
import random

"""Ugly testing script
"""

def read_graph():
    with open("test_graph.txt") as graph:
        graph = graph.read()
        graph = graph.split('\n')
        graph = [line.split(" ") for line in graph]
        return graph

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
    gr.build_graph("test/test_graph.txt")
    print(gr) # only print the graph to check results

def test_path():
    p1 = Path(Node(0), 0.6)
    p2 = Path(Node(0), 0.5)
    assert p1 > p2

def  test_priority_q():
    pq = PriorityQueue()
    gr = Graph()
    gr.build_graph("test/test_graph.txt")
    random.seed(777)
    for _, value in gr.node_map.items():
        value.dist = random.random()
        pq.push(Path(value, value.dist))
    res = []
    while len(pq._queue)>0:
        node_out = pq.pop()
        res.append(int(node_out.id))
    assert res == [6, 2, 3, 5, 4, 1]

    

