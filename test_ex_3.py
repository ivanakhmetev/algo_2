from ex_3 import BST, BSTNode

def test_init():
    root = BSTNode(8, 'root', None)
    tree = BST(root)
    tree.AddKeyValue(4, 'l1')
    tree.AddKeyValue(2, 'l11')
    tree.AddKeyValue(1, 'l111')
    tree.AddKeyValue(10, 'r1')
    assert tree.Root.NodeKey == 8
    assert tree.Root.LeftChild.NodeKey == 4
    assert tree.Root.RightChild.NodeKey == 10
    return tree

def test_wide():
    tree = test_init()
    nodes = tree.WideAllNodes()
    test_nodes = [8, 4, 10, 2, 1]
    for i in range(len(nodes)):
        assert nodes[i].NodeKey == test_nodes[i]

def test_inorder():
    tree = test_init()
    nodes = tree.DeepAllNodes(0)
    test_nodes = [1, 2, 4, 8 ,10]
    for i in range(len(nodes)):
        assert nodes[i].NodeKey == test_nodes[i]


        