# This file left intentionally blank.
from queue2050 import Queue
from stack2050 import Stack

class Graph:
    def __init__(self, V=None, E=None):
        raise NotImplementedError("graph class should not be used directly, use AdjacencySetGraph or EdgeSetGraph.")

    def connected(self, v1, v2):
        visited = set()
        def dfs(v):
            if v == v2:
                return True
            visited.add(v)
            for neighbor in self.neighbors(v):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(v1)
    
    def bfs(self, start):
        queue = Queue()
        visited = {start: None}
        queue.enqueue(start)
        while not queue.is_empty():
            current = queue.dequeue()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.enqueue(neighbor)
        return visited
    
    def dfs(self, start):
        stack = Stack()
        visited = {start: None}
        stack.push(start)
        while not stack.is_empty():
            current = stack.pop()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    stack.push(neighbor)
        return visited

    def shortest_path(self, v1, v2):
        queue = Queue()
        queue.enqueue((v1, 0, []))
        visited = set([v1])
        while not queue.is_empty():
            current, dist, path = queue.dequeue()
            if current == v2:
                return (dist, path)
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue((neighbor, dist + 1, path + [(current, neighbor)]))
        return (float("inf"), None)

    def has_cycle(self):
        visited = set()
        path = []
        def visit(vertex):
            if vertex in path:
                return True, path[path.index(vertex):] + [vertex]
            if vertex in visited:
                return False, None
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.neighbors(vertex):
                has_cycle, cycle_path = visit(neighbor)
                if has_cycle:
                    return True, cycle_path
            path.pop()
            return False, None
        for v in self:
            if v not in visited:
                has_cycle, cycle_path = visit(v)
                if has_cycle:
                    cycle_edges = [(cycle_path[i], cycle_path[i + 1]) for i in range(len(cycle_path) - 1)]
                    return True, cycle_edges
        return False, None


class AdjacencySetGraph(Graph):
    """Store a dictionary of vertex:set(vertices) pairs, to allow fast iteration over neighbors."""
    def __init__(self, V=None, E=None):
        """initiates graph with set of vertices and set of edges."""
        self.adjacent_dict = {v: set() for v in V}
        for e in E: self.add_edge(e)
    
    def __iter__(self):
        """returns an iterator over all vertices in the graph."""
        return iter(self.adjacent_dict.keys())
    
    def add_vertex(self, v):
        """add vertex v to graph."""
        if v not in self.adjacent_dict:
            self.adjacent_dict[v] = set()
    
    def add_edge(self, e):
        """add edge e to graph."""
        u,v = e
        if u not in self.adjacent_dict:
            self.add_vertex(u)
        if v not in self.adjacent_dict:
            self.add_vertex(v)
        self.adjacent_dict[u].add(v)
    
    def neighbors(self, v):
        """returns iterator over all neighbors of v."""
        return iter(self.adjacent_dict[v])


class EdgeSetGraph(Graph):
    """store a set of vertices and a set of edges instead of a dictionary of vertex:set(neighbors) pairs."""
    def __init__(self, V=None, E=None):
        """initiates graph with set of vertices and set of edges."""
        self.V = V if V else set()
        self.E = E if E else set()
    
    def __iter__(self):
        """returns an iterator over all vertices in the graph."""
        return iter(self.V)

    def add_vertex(self, v):
        """add vertex v to graph."""
        self.V.add(v)
    
    def add_edge(self, e):
        """add edge e to graph."""
        u, v = e
        if u in self.V and v in self.V:
            self.E.add((u, v))

    def neighbors(self, v):
        """returns iterator over all neighbors of v."""
        #return vertex u for each edge tuple in edge set if one vertex is equal to v (meaning it is neighbor)
        return (w for u,w in self.E if u==v)