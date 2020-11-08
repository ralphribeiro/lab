from typing import Pattern
import weakref


class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def __repr__(self):
        return f'nó({self._value})'

    def __iter__(self):
        return iter(self._children)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self._children.append(child)
        child.parent = self

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
