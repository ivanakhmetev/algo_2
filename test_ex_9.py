from ex_9 import SimpleTree, SimpleTreeNode

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
    r4 = SimpleTreeNode(25, r3)
    tree.AddChild(r1, r2)
    tree.AddChild(r2, r3)
    tree.AddChild(r3, r4)
    return tree

def test_iseven():
    t = init_tree()
    assert t.IsEven() is True
    t1 = SimpleTree(t.Root.Children[1])
    # print(t1.Root.NodeValue, t1.Root.Children[0].NodeValue, t1.Root.Children[0].Children[0].NodeValue,  t1.Root.Children[0].Children[0].Children)
    assert t1.IsEven() is True
    assert t.EvenTrees() == [9, 17]