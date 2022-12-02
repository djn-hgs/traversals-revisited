class Queue:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def __contains__(self, item):
        return item in self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []


class Node:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        if self.name:
            return f'Node <"{self.name}">'
        else:
            return 'Node <blank>'


class Edge:
    def __init__(self, start, end, directed=False, weight=None):
        self.start = start
        self.end = end
        self.directed = directed
        self.weight = weight

    def __repr__(self):
        return f'Edge from {self.start} to {self.end}' \
                f'{" directed" if self.directed else ""}' \
                f'{" weight" if self.weight else ""}'


class Graph:
    @classmethod
    def from_edge_list(cls, edges):
        my_graph = Graph()

        for e in edges:
            my_graph.add_edge(e)

        return my_graph

    def __init__(self):
        self.adjacency_matrix = {}

    def __contains__(self, item):
        return item in self.adjacency_matrix

    def add_node(self, node):
        if node in self.adjacency_matrix:
            raise ValueError('Node already in graph.')
        else:
            self.adjacency_matrix[node] = {}

    def add_edge(self, edge):
        if edge.start not in self.adjacency_matrix:
            self.add_node(edge.start)

        if edge.end not in self.adjacency_matrix:
            self.add_node(edge.end)

        self.adjacency_matrix[edge.start][edge.end] = {'directed': edge.directed,
                                                       'weight': edge.weight
                                                       }

    def neighbours(self, node):
        if node in self.adjacency_matrix:
            return self.adjacency_matrix[node]
        else:
            raise Exception(f'{node} not in graph {self}')


class Traversal:
    def __init__(self, graph, root):
        self.graph = graph

        if root in graph:
            self.root = root
        else:
            raise Exception(f'Root node <{self.root}> is not in Graph <{self.graph}>.')

        self.visited = []

    def tick(self):
        """This should implement one step in the relevant traversal.
        """


class BreadthFirstTraversal(Traversal):
    def __init__(self, graph, root):
        super().__init__(graph, root)
        self.queue = Queue()

        self.queue.enqueue(root)
        self.visited.append(root)

    def tick(self):
        node = self.queue.dequeue()

        for neighbour in self.graph.neighbours(node):
            if neighbour not in self.visited:
                self.queue.enqueue(neighbour)
                self.visited.append(neighbour)

    def run_to_end(self):
        while self.queue:
            self.tick()

