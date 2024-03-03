from ex_7 import Heap


def test_init():
    a = Heap()
    a.MakeHeap([1,2,3], 1)
    assert a.HeapArray == [3, 2, 1]

def test_getmax():
    a = Heap()
    a.MakeHeap([11,9,4,3,1,7,8,2,5,6,], 3)
    assert a.HeapArray[:7] == [11,9,8,7,6,5,4]
    max = a.GetMax()
    assert max == 11
    assert a.HeapArray[:9] == [9, 7, 8, 3, 6, 5, 4, 1, 2]

def test_add():
    a = Heap()
    a.MakeHeap([1,2,3,4], 2)
    a.Add(5)
    assert a.HeapArray ==  [5, 3, 4, 1, None, None, 2]
