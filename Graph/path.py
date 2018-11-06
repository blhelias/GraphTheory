class Path:
    """Usefull class used by PriorityQueue
    """

    def __init__(self, dest: "Node", cost: float):
        self.dest = dest
        self.cost = cost

    def __lt__ (self, other: "Path"):
        return self.cost < other.cost
    
    def __eq__(self, other: "Path"):
        return self.cost == other.cost