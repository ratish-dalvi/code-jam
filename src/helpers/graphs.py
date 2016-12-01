# Implementation of an undirected graph


class Graph:
    """
    Graph implemented by a dict of lists.
      {
        0 : [2, 3],
        1 : [2],
        2 : [3]
      }
    Implementation favourable for a heavily connected graph with a large
    number of nodes
    """
    def __init__(self, x=None):
        if isinstance(x, int):
            self._items = {i: [] for i in range(x)}
        elif isinstance(x, list):
            self._items = {i: [] for i in x}
        else:
            raise Exception("Unrecognized argument")

    def add_unidrected_edge(self, a, b):
        self._items[a].append(b)
        self._items[b].append(a)

    def num_connected_components(self):
        unvisited = set(self._items.keys())
        cnt = 0
        q = []  # We don't need a FIFO queue
        while len(unvisited):
            q.append(unvisited.pop())
            while len(q):
                x = q.pop()
                for i in self._items[x]:
                    if i in unvisited:
                        unvisited.remove(i)
                        q.append(i)
            cnt += 1
        return cnt
