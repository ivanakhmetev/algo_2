from ex_2 import BST, BSTNode

def test_init():
    root = BSTNode(8, 'root', None)
    tree = BST(root)
    tree.AddKeyValue(4, 'l1')
    tree.AddKeyValue(2, 'l11')
    tree.AddKeyValue(1, 'l111')


