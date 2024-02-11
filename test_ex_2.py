from ex_2 import BST, BSTNode

def test_init():
    root = BSTNode(8, 'root', None)
    tree = BST(root)
    tree.AddKeyValue(4, 'l1')
    tree.AddKeyValue(2, 'l11')
    tree.AddKeyValue(1, 'l111')
    return tree


def test_find():
    tree = test_init()
    find_bigger = tree.FindNodeByKey(20)
    assert find_bigger.Node is not None and find_bigger.NodeHasKey is False and find_bigger.ToLeft is False
    find_smaller = tree.FindNodeByKey(0)
    assert find_smaller.Node is not None and find_smaller.NodeHasKey is False and find_smaller.ToLeft is True
    find_exist = tree.FindNodeByKey(2)
    assert find_exist.Node is not None and find_exist.NodeHasKey is True and find_exist.ToLeft is False

def test_add():
    tree = test_init()
    find_non_exist = tree.FindNodeByKey(5)
    assert find_non_exist.NodeHasKey is False
    tree.AddKeyValue(5, 'l1r')
    find_exist = tree.FindNodeByKey(5)
    assert find_exist.NodeHasKey is True
    assert find_exist.Node.Parent == tree.Root.LeftChild
    find_non_exist = tree.FindNodeByKey(10)
    assert find_non_exist.NodeHasKey is False
    tree.AddKeyValue(10, 'r1')
    find_exist = tree.FindNodeByKey(10)
    assert find_exist.Node.Parent == tree.Root
    assert find_exist.NodeHasKey is True

    empty_tree = BST(None)
    find_non_exist = empty_tree.FindNodeByKey(8)
    assert find_non_exist.Node is None
    empty_tree.AddKeyValue(8, 'rott')
    find_root = empty_tree.FindNodeByKey(8)
    assert find_root.Node == empty_tree.Root



def test_count():
    tree = test_init()
    assert tree.Count()== 4

def test_finminmax():
    tree = test_init()
    find = tree.FinMinMax(tree.Root, True)
    assert find.NodeKey == 8
    find = tree.FinMinMax(tree.Root, False)
    assert find.NodeKey == 1
    tree.AddKeyValue(5, 'l1r')
    find = tree.FinMinMax(tree.Root.LeftChild, True)
    assert find.NodeKey == 5
    find = tree.FinMinMax(tree.Root.LeftChild, False)
    assert find.NodeKey == 1
    tree.AddKeyValue(3, 'l1r')
    find = tree.FinMinMax(tree.Root.LeftChild, True)
    assert find.NodeKey == 5
    tree.DeleteNodeByKey(5)
    find = tree.FinMinMax(tree.Root.LeftChild, True)
    assert find.NodeKey == 4
    find = tree.FinMinMax(tree.Root.LeftChild.LeftChild, True)
    assert find.NodeKey == 3
    find = tree.FinMinMax(tree.Root.LeftChild.LeftChild, False)
    assert find.NodeKey == 1

def test_delete():
    tree = test_init()
    assert tree.Count() == 4
    tree.DeleteNodeByKey(1)
    assert tree.Count() == 3
    tree.DeleteNodeByKey(4)
    assert tree.Count() == 2
    tree.DeleteNodeByKey(8)
    assert tree.Count() == 1
    tree.DeleteNodeByKey(2)
    assert tree.Count() == 0

def test_delete_2():
    tree = test_init()
    assert tree.Count() == 4
    tree.DeleteNodeByKey(8)
    assert tree.Count() == 3

def test_delete_3():
    tree = test_init()
    assert tree.Count() == 4
    tree.DeleteNodeByKey(4)
    assert tree.Count() == 3
    tree.AddKeyValue(10, 'r1')
    assert tree.Count() == 4
    tree.DeleteNodeByKey(10)
    assert tree.Count() == 3
    tree = BST(BSTNode(8, 'root', None))
    assert tree.Count() == 1
    tree.DeleteNodeByKey(8)
    assert tree.Count() == 0
    tree.AddKeyValue(3, 'root')
    tree.AddKeyValue(4, 'r1')
    assert tree.Count() == 2
    tree.DeleteNodeByKey(4)
    assert tree.Count() == 1







    
