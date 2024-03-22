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
    
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, elem):
        self.s1.push(elem)

    def dequeue(self):
        if not self.s1 and not self.s2:
            return None
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()
    
    def size(self):
        if self.s1.len() == 0 and self.s2.len() == 0:
            return 0
        if self.s1.len() == 0 and self.s2.len() != 0:
            return self.s2.len()
        if self.s1.len() != 0 and self.s2.len() == 0:
            return self.s1.len()
        





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
        self.stack = Stack()
        self.SetUnhit()
        self.step_1(VFrom, VTo)
        return [self.vertex[i] for i in self.stack.stack]


    def step_1(self, current, VTo):
        self.vertex[current].Hit = True
        self.stack.push(current)
        adjacency = self.m_adjacency[current]
        # print('stack',self.stack.stack)
        # print('curr adj', adjacency)
        self.step_4(adjacency, VTo)
        



    def step_4(self, adjacency, VTo):
        if adjacency[VTo] == 1:
            self.stack.push(VTo)
            # print(self.stack.stack)
            return
            # return self.stack
        if adjacency[VTo] == 0:
            unvisit_neighbours = [i for i in range(len(adjacency)) if self.vertex[i].Hit is False and adjacency[i] == 1]
            # print('unvisit', unvisit_neighbours)
            # print(unvisit_neighbours)
            if len(unvisit_neighbours) != 0:
                self.step_1(unvisit_neighbours[0], VTo)
            if len(unvisit_neighbours) == 0:
                # print('len')
                self.stack.pop()
                if self.stack.len() == 0:
                    return []
                if self.stack.len() != 0:
                    new_current = self.stack.pop()
                    self.step_1(new_current, VTo)


        # self._DepthFirstSearch(VFrom, VTo, stack)


        # if self._DepthFirstSearch(VFrom, VTo, stack) is True:
        #     return stack
        # for i in range(len(self.m_adjacency[VFrom])): #4
        #     if self.m_adjacency[i] == 1 and self.vertex[i].Hit == False:
        #         if self._DepthFirstSearch(i, VTo, stack) is True:
        #             return stack
        # stack.pop()
        # if stack.len() == 0:
        #     return []
        # for i 
                

        # current = self.vertex[VFrom]
        # current.Hit = True
        # stack.push(VFrom)
        # collumn = self.m_adjacency[VFrom]
        # for i in range(len(collumn)):
        #     if collumn[i] == 1 and i == VTo:
        #         stack.push(VTo)
        #         return stack
    #     for i in range(len(collumn)):
    #         if collumn[i] == 1 and self.vertex[i].Hit == False:
    #             current = self.vertex[i]
        
    # def _DepthFirstSearch(self, current, VTo, stack):
    #     self.vertex[current].Hit = True
    #     stack.push(current)
    #     neighbours = self.m_adjacency[current]
    #     if neighbours[VTo] == 1:
    #         stack.push(VTo)
    #         return
    #     stack.pop()
    #     return
    
        # for i in range(len(collumn)):
        #     if collumn[i] == 1 and i == VTo:
        #         stack.push(VTo)
        #         return True
        # return False


        
    def BreadthFirstSearch(self, VFrom, VTo):
        # path = []
        self.queue = Queue()
        self.SetUnhit()


        self.vertex[VFrom].Hit = True
        self.queue.enqueue([VFrom])
        # path.append(VFrom)
        while self.queue.size() is not None:
            path = self.queue.dequeue()
            current = path[-1]
            adjacency = self.m_adjacency[current]
            unvisit_neighbours = [i for i in range(len(adjacency)) if self.vertex[i].Hit is False and adjacency[i] == 1]

            for el in unvisit_neighbours:
                new_path = list(path)
                new_path.append(el)
                self.queue.enqueue(new_path)
                if el == VTo:
                    return [self.vertex[i] for i in new_path]
                    
        
        return []
                # if el not in path:
                #     path.append(el)
                # self.vertex[el].Hit = True
                # self.queue.enqueue(el)
                # return path



    def SetUnhit(self):
        for el in self.vertex:
            if el is not None:
                el.Hit = False

