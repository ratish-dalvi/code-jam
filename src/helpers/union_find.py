"""UnionFind.py

Union-find data structure. Based on Josiah Carlson's code,
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
with significant additional changes by David Eppstein (UC Irvine).
Some minor pep-8ing changes by R. Dalvi
"""


class UnionFind:
    """Union-find data structure.

    Supports:
    - Union by rank
    - Path compression

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, x):
        """Find and return the name of the set containing the x."""

        # check for previously unknown x
        if x not in self.parents:
            self.parents[x] = x
            self.weights[x] = 1
            return x

        # find path of x leading to the root
        path = [x]
        root = self.parents[x]
        prev = x
        while root != prev:
            path.append(root)
            prev = root
            root = self.parents[root]

        # path compression
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def number_of_roots(self):
        """ Get the number of nodes without any parents
        """
        cnt = 0
        for k, v in self.parents.iteritems():
            if k == v:
                cnt += 1
        return cnt

    def number_of_items(self):
        return len(self.parents)

    def union(self, *items):
        """Find the sets containing the items and merge them all."""
        roots = [self[x] for x in items]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
