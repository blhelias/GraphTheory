import heapq


class PriorityQueue:
    """ Implement our priorityQueue (pq) that uses edge cost as key sorting
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, path):
        """Add element to the pq

        Arguments:
            path {Path}
        """
        heapq.heappush(self._queue, (path.cost, self._index, path.dest))
        self._index += 1

    def pop(self):
        """Remove element from our pq

        Returns:
            Node
        """
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        """Check if our pq is empty

        Returns:
            Boolean
        """

        return len(self._queue) == 0
