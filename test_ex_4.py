from ex_4 import aBST

def test_init():
    tree = aBST(0)
    assert len(tree.Tree) == 1
    tree = aBST(3)
    assert len(tree.Tree) == 15

def test_haschild():
    tree = aBST(3)
    assert tree.is_next_lvl(6) is True
    assert tree.is_next_lvl(8) is False

def test_find():
    tree = aBST(0)
    assert tree.FindKeyIndex(3) is None
    tree.Tree[0] = 1
    assert tree.FindKeyIndex(1) == 0
    tree = aBST(1)
    tree.Tree[0] = 50
    tree.Tree[1] = 25
    tree.Tree[2] = 75
    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    tree = aBST(3)
    tree.Tree[0] = 50
    tree.Tree[1] = 25
    tree.Tree[2] = 75
    tree.Tree[3] = None
    tree.Tree[4] = 37
    tree.Tree[5] = 62
    tree.Tree[6] = 84
    tree.Tree[7] = None
    tree.Tree[8] = None
    tree.Tree[9] = 31
    tree.Tree[10] = 43
    tree.Tree[11] = 55
    tree.Tree[12] = None
    tree.Tree[13] = None
    tree.Tree[14] = 92
    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    assert tree.FindKeyIndex(37) == 4
    assert tree.FindKeyIndex(62) == 5
    assert tree.FindKeyIndex(84) == 6
    assert tree.FindKeyIndex(31) == 9
    assert tree.FindKeyIndex(43) == 10
    assert tree.FindKeyIndex(92) == 14
    assert tree.FindKeyIndex(20) == -3
    assert tree.FindKeyIndex(64) == -12

def test_add():
    tree = aBST(3)
    tree.AddKey(50)
    tree.AddKey(25)
    tree.AddKey(75)
    print(tree.Tree[0], tree.Tree[1], tree.Tree[2])
    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    tree.AddKey(37)
    tree.AddKey(62)
    tree.AddKey(84)
    tree.AddKey(31)
    tree.AddKey(43)
    tree.AddKey(55)
    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    assert tree.FindKeyIndex(37) == 4
    assert tree.FindKeyIndex(62) == 5
    assert tree.FindKeyIndex(84) == 6
    assert tree.FindKeyIndex(31) == 9

