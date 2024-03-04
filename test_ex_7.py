from ex_7 import Heap


def test_init():
    a = Heap()
    a.MakeHeap([1,2,3], 1)
    assert a.HeapArray == [3, 1, 2]

def test_getmax():
    a = Heap()
    a.MakeHeap([11,9,4,3,1,7,8,2,5,6,], 3)
    assert a.HeapArray ==  [11, 6, 9, None, 5, 8, 4, None, None, None, None, 2, 7, 1, 3]
    max = a.GetMax()
    assert max == 11
    assert a.HeapArray ==  [9, 6, 8, None, 5, 7, 4, None, None, None, None, 2, 3, 1, None]

def test_add():
    a = Heap()
    a.MakeHeap([1,2,3,4], 2)
    a.Add(5)
    assert a.HeapArray ==  [5, 4, 3, None, None, 2, 1]

def test_bobrobski():
    a = Heap()
    a.MakeHeap([110, 90,40, 70,80, 30,10, 20,50, 60,65, 31,29, 11,9] ,3)
    assert a.HeapArray == [110, 90,40, 70,80, 31,11, 20,50, 60,65, 30,29, 10,9]

# test_init()
