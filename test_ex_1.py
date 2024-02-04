from ex_1 import SimpleTree, SimpleTreeNode

def init_tree():

    root = SimpleTreeNode(9, None)
    tree = SimpleTree(root)
    l1 = SimpleTreeNode(4, root)
    r1 = SimpleTreeNode(17, root)
    tree.AddChild(root, l1)
    tree.AddChild(root, r1)
    l2l = SimpleTreeNode(3, l1)
    l2r = SimpleTreeNode(6, l1)
    tree.AddChild(l1, l2l)
    tree.AddChild(l1, l2r)
    l3l = SimpleTreeNode(5, l2r)
    l3r = SimpleTreeNode(7, l2r)
    tree.AddChild(l2r, l3l)
    tree.AddChild(l2r, l3r)
    r2 = SimpleTreeNode(22, r1)
    r3 = SimpleTreeNode(20, r2)
    tree.AddChild(r1, r2)
    tree.AddChild(r2, r3)
    return tree

def test_init_tree():

    tree = init_tree()

    assert [el.NodeValue for el in tree.Root.Children] == [4, 17]
    assert [el.NodeValue for el in tree.Root.Children[0].Children] == [3, 6]
    assert tree.Root.Children[0].Parent.NodeValue == 9
    assert tree.Root.Children[1].Parent.NodeValue == 9
    assert [el.NodeValue for el in tree.Root.Children[1].Children] == [22]

def test_delete_node():

    tree = init_tree()
    tree.DeleteNode(tree.Root)
    assert [el.NodeValue for el in tree.Root.Children] == [4, 17]
    tree.DeleteNode(tree.Root.Children[0])
    assert [el.NodeValue for el in tree.Root.Children] == [ 17]
    tree.DeleteNode(tree.Root.Children[0])
    assert [el.NodeValue for el in tree.Root.Children] == []

def test_get_all_nodes():
    tree = init_tree()
    nodes = tree.GetAllNodes()
    l1 = sorted([el.NodeValue for el in nodes])
    l2 = sorted([9, 4, 3, 6, 5, 7, 17, 22, 20])
    assert l1 == l2

def test_get_nodes_by_value():

    tree = init_tree()
    nodes_by_7 = tree.FindNodesByValue(7)
    assert [el.NodeValue for el in nodes_by_7] == [7]

def test_move_node():
    tree = init_tree()
    tree.MoveNode(tree.Root.Children[0], tree.Root.Children[1])
    l1 = sorted([el.NodeValue for el in tree.Root.Children])
    l2 = sorted([17])
    l3 = sorted([22, 4])
    l4 = sorted([el.NodeValue for el in tree.Root.Children[0].Children])
    assert l1 == l2 
    assert l3 == l4

def test_count_nodes():
    tree = init_tree()
    assert tree.Count() == 9

def test_count_leafs():
    tree = init_tree()
    assert tree.LeafCount() == 4