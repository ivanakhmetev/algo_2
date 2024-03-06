class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        i = self._FindVertex(None)
        self.vertex[i] = Vertex(v)
	
    def RemoveVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is not None:
                self.RemoveEdge(v, i)
        self.vertex[v] = None

    def IsEdge(self, v1, v2):
        return bool(self.m_adjacency[v1, v2])

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1] [v2] = 1
        self.m_adjacency[v2] [v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1] [v2] = 0
        self.m_adjacency[v2] [v1] = 0

    def _FindVertex(self, v):
        if v in self.vertex:
            return self.vertex.index(v)