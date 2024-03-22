from ex_12 import Vertex, SimpleGraph

def test_init():
    # v1 = Vertex(2)
    # v2 = Vertex(4)
    g = SimpleGraph(5)
    g.AddVertex(2)
    g.AddVertex(4)
    assert g.vertex[0].Value == 2
    assert g.vertex[1].Value == 4
    assert g.m_adjacency[0] [1] == 0
    assert g.m_adjacency[1] [0] == 0
    return g

def test_add_adj():
    g = test_init()
    g.AddEdge(0, 1)
    assert g.m_adjacency[0] [1] == 1
    assert g.m_adjacency[1] [0] == 1
    return g

def test_delete_adj():
    g = test_add_adj()
    g.RemoveEdge(0, 1)
    assert g.m_adjacency[0] [1] == 0
    assert g.m_adjacency[1] [0] == 0

def test_delete_v():
    g = test_init()
    g.RemoveVertex(0)
    assert g.vertex[0] == None
    assert g.m_adjacency[0] [1] == 0
    assert g.m_adjacency[1] [0] == 0

def init_graph():
    g = SimpleGraph(5)
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    g.AddVertex(a)
    g.AddVertex(b)
    g.AddVertex(c)
    g.AddVertex(d)
    g.AddVertex(e)
    # g.AddEdge(0, 1)
    # g.AddEdge(0, 2)
    g.AddEdge(0, 3)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)
    return g

def init_2():
    g = SimpleGraph(9)
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    b1 = Vertex('b1')
    c1 = Vertex('c1')
    d1 = Vertex('d1')
    e1 = Vertex('e1')
    g.AddVertex(a)
    g.AddVertex(b)
    g.AddVertex(c)
    g.AddVertex(d)
    g.AddVertex(e)
    g.AddVertex(b1)
    g.AddVertex(c1)
    g.AddVertex(d1)
    g.AddVertex(e1)
    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)
    g.AddEdge(1, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4  )
    g.AddEdge(4, 5)
    g.AddEdge(2, 5)
    g.AddEdge(5, 6)
    g.AddEdge(5, 7)
    g.AddEdge(6, 7)
    g.AddEdge(7, 8)
    return g


g = init_2()
# print(g.BreadthFirstSearch(0, 4))
# print(g.WeakVertices())
# for el in a.m_adjacency:
#     print(el)
b = g.WeakVertices()
for el in b:
    print(el.Value.Value)
# print(a.DepthFirstSearch(4,1))

