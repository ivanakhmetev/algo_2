from ex_10 import Vertex, SimpleGraph

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
    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(0, 3)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)
    return g

a = init_graph()
for el in a.m_adjacency:
    print(el)

print(a.DepthFirstSearch(4,1))

