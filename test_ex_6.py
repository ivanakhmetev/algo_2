
from ex_6 import BalancedBST

def test_1():
    a = [1, 2, 3]
    b = BalancedBST()
    b.GenerateTree(a)
    # print(b)
    assert b.Root.NodeKey == 2
    assert b.Root.Level == 0
    assert b.Root.LeftChild.NodeKey == 1
    assert b.Root.RightChild.NodeKey == 3
    assert b.Root.LeftChild.Level == 1
    assert b.Root.RightChild.Level == 1
    assert b.IsTreeCorrect() == True


# def test_2():
#     a = [0, 1, 2, 3, 4, 5]
#     b = GenerateBBSTArray(a)
#     print(b)
#     assert b[0] == 3
#     assert b[1] == 1
#     assert b[2] == 5
#     assert b[3] == 0
#     assert b[4] == 2
#     assert b[5] == 4

# def test_3():
#     a = []
#     b = GenerateBBSTArray(a)
#     assert b == []

# def test_4():
#     a = [1]
#     b = GenerateBBSTArray(a)
#     assert b == [1]

# def test_5():
#     a = [1,10]
#     b = GenerateBBSTArray(a)
#     assert b == [10, 1, None]

# def test_6():
#     # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     a = [1, 2, 3, 4, 5, 6, 7]
#     b = GenerateBBSTArray(a)
#     print(b)
#     assert b == [4, 2, 6, 1, 3, 5, 7]

def test_7():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = BalancedBST()
    b.GenerateTree(a)
    # print(b)
    assert b.Root.NodeKey == 5

    assert b.Root.LeftChild.NodeKey == 2
    assert b.Root.RightChild.NodeKey == 8

    assert b.Root.LeftChild.LeftChild.NodeKey == 1
    assert b.Root.LeftChild.RightChild.NodeKey == 4
    assert b.Root.RightChild.LeftChild.NodeKey == 7
    assert b.Root.RightChild.RightChild.NodeKey == 10
    assert b.Root.RightChild.RightChild.Level == 2

    assert b.Root.LeftChild.LeftChild.LeftChild.NodeKey == 0
    assert b.Root.LeftChild.LeftChild.LeftChild.Level == 3
    assert b.Root.LeftChild.LeftChild.RightChild == None
    assert b.Root.LeftChild.RightChild.LeftChild.NodeKey == 3
    assert b.Root.LeftChild.RightChild.RightChild == None
    
    assert b.Root.RightChild.LeftChild.LeftChild.NodeKey == 6
    assert b.Root.RightChild.LeftChild.RightChild == None
    assert b.Root.RightChild.RightChild.LeftChild.NodeKey == 9
    assert b.Root.RightChild.RightChild.RightChild == None
    assert b.IsTreeCorrect() == True
    assert b.IsBalanced(b.Root) == True
    b.Root.LeftChild.Parent = None
    b.Root.LeftChild.LeftChild = None
    b.Root.LeftChild.RightChild = None
    b.Root.LeftChild = None
    assert b.IsBalanced(b.Root) == False

    # assert b == [5, 2, 8, 1, 4, 7, 10, 0, None, 3, None, 6, None, 9, None]


