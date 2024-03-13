class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()
    
    def len(self):
        return len(self.stack)

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
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
        return bool(self.m_adjacency[v1] [v2])

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1] [v2] = 1
        self.m_adjacency[v2] [v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1] [v2] = 0
        self.m_adjacency[v2] [v1] = 0

    def _FindVertex(self, v):
        if v in self.vertex:
            return self.vertex.index(v)
        
    def DepthFirstSearch(self, VFrom, VTo):
        stack = Stack()
        self.SetUnhit()
        if self._DepthFirstSearch(VFrom, VTo, stack) is True:
            return stack
        for i in range(len(self.m_adjacency[VFrom])): #4
            if self.m_adjacency[i] == 1 and self.vertex[i].Hit == False:
                if self._DepthFirstSearch(i, VTo, stack) is True:
                    return stack
        stack.pop()
        if stack.len() == 0:
            return []
        for i 
                

        # current = self.vertex[VFrom]
        # current.Hit = True
        # stack.push(VFrom)
        # collumn = self.m_adjacency[VFrom]
        # for i in range(len(collumn)):
        #     if collumn[i] == 1 and i == VTo:
        #         stack.push(VTo)
        #         return stack
        for i in range(len(collumn)):
            if collumn[i] == 1 and self.vertex[i].Hit == False:
                current = self.vertex[i]
        
    def _DepthFirstSearch(self, current, VTo, stack):
        stack.push(current)
        collumn = self.m_adjacency[current]
        for i in range(len(collumn)):
            if collumn[i] == 1 and i == VTo:
                stack.push(VTo)
                return True
        return False


        



        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        pass

    def SetUnhit(self):
        for el in self.vertex:
            if el is not None:
                el.Hit = False