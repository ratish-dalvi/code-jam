# Implementation of a queue
class Queue:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def add(self, item):
        self._items.insert(0, item)

    def remove(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def remove_all(self):
        self._items = []
