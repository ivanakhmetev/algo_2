class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        return self._FindNodeByKey(self.Root, key)

    def _FindNodeByKey(self, node, key):
        if key < node.NodeKey and node.LeftChild is not None:
            return self._FindNodeByKey(node.LeftChild, key)
        if key > node.NodeKey and node.RightChild is not None:
            return self._FindNodeByKey(node.RightChild, key)
        find = BSTFind()
        if key < node.NodeKey and node.LeftChild is None:
            find.Node = node
            find.ToLeft = True
        if key > node.NodeKey and node.RightChild is None:
            find.Node = node
        if key == node.NodeKey:
            find.Node = node
            find.NodeHasKey = True
        return find

    def AddKeyValue(self, key, val):
        find = self.FindNodeByKey(key)
        if find.NodeHasKey is True:
            return False
        if find.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        if find.ToLeft is True:
            find.Node.LeftChild = BSTNode(key, val, find.Node)
            return True
        if find.ToLeft is False:
            find.Node.RightChild = BSTNode(key, val, find.Node)
            return True
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None
	
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self):
        return 0 # количество узлов в дереве