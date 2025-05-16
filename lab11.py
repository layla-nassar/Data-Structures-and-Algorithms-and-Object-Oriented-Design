class Graph_AS:
    def __init__(self, V, E):
        """initializes with optional sets of vertices V and edges E"""
        self.g = {}
        for vertex in V:
            self.g[vertex] = set()
        for edge in E:
            self.g[edge[0]].add(edge[1])
    
    def __len__(self):
        """Return the number of vertices in the graph"""
        return len(self.g)
    
    def __iter__(self):
        """iterates over all vertices in graph"""
        for vertex in self.g:
            yield vertex

    def add_vertex(self, v):
        """Adds vertex v to graph"""
        if v not in self.g:
            self.g[v] = set()

    def remove_vertex(self, v):
        """Removes vertex v from graph, raise a KeyError if v is not in graph"""
        del self.g[v]
        for vertex in self.g.values():
            vertex.remove(v)

    def add_edge(self, e):
        """Adds edge e to graph"""
        self.g[e[0]].add(e[1])


    def remove_edge(self, e):
        """Removes edge e from graph, raise a KeyError if e is not in graph"""
        self.g[e[0]].remove(e[1])


    def _neighbors(self, v):
        """returns an iterable collection of neighbors of vertex v"""
        #for vertex in self.g[v]:
            #yield vertex
        return iter(self.g[v])

class Graph_ES:
    def __init__(self, V=None, E=None):
        self.vertices = set()
        self.edges = set()
        if V is not None:
           for v in V: self.add_vertex(v)
        if E is not None:
           for e in E: self.add_edge(e)
         
    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, v):
        self.vertices.add(v)
   
    def remove_vertex(self, v):
        if v not in self.vertices:
           raise KeyError("V is not in graph")
        self.vertices.remove(v) 
   
    def add_edge(self, e):
        self.edges.add(e)
   
    def remove_edge(self, e):
        if e not in self.edges:
           raise KeyError("E is not in graph")
        self.edges.remove(e)
    
    def _neighbors(self, v):
        return {y for x, y in self.edges if x == v} 
