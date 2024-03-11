'''algo_2 ex_1 general tree implementation'''

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
    tree.AddChild(r1, r2)
    tree.AddChild(r2, r3)
    r4 = SimpleTreeNode(25, r3)
    tree.AddChild(r3, r4)
    return tree
            
def test_iseven():
    tree = init_tree()    
    assert tree.IsEven() is True

def test_even():
    tree = init_tree()
    even = tree.EvenTrees()
    assert even[0].NodeValue == 9
    assert even[1].NodeValue == 17
