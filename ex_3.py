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
        if self.Root is None:
            return BSTFind()
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

    def _FindMin2(self, node, FindMax):
        find = BSTFind()
        if node.LeftChild is None and node.RightChild is None:
            find.Node = node
            return find
        if node.LeftChild is not None and FindMax is False:
            return self._FindMin2(node.LeftChild, FindMax)
        if node.LeftChild is None and FindMax is False:
            return self._FindMin2(node.RightChild, FindMax)
        if node.RightChild is not None and FindMax is True:
            return self._FindMin2(node.RightChild, FindMax)
        if node.RightChild is None and FindMax is True:
            return self._FindMin2(node.LeftChild, FindMax)


    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return BSTNode(None, None, None)
        if FindMax:
            return self._FindMax(FromNode)
        else:
            return self._FindMin(FromNode)

    def _FindMin(self, node):
        if node.LeftChild is not None:
            return self._FindMin(node.LeftChild)
        return node

    def _FindMax(self, node):
        if node.RightChild is not None:
            return self._FindMax(node.RightChild)
        return node
    
    def _DeleteNodeByKey(self, root, key):
        if root is None:
            return root
        
        if key < root.NodeKey:
            root.LeftChild = self._DeleteNodeByKey(root.LeftChild, key)
            if root.LeftChild is not None:
                root.LeftChild.Parent = root

        elif key > root.NodeKey:
            root.RightChild = self._DeleteNodeByKey(root.RightChild, key)
            if root.RightChild is not None:
                root.RightChild.Parent = root
            
        else:
            if root.LeftChild is None:
                temp = root.RightChild
                return temp
            
            elif root.RightChild is None:
                temp = root.LeftChild
                return temp
            
            temp = self.FinMinMax(root.RightChild, False)
            root.NodeKey = temp.NodeKey
            root.NodeValue = temp.NodeValue
            root.RightCHild = self._DeleteNodeByKey(root.RightChild, temp.NodeKey)
        return root


    def DeleteNodeByKey(self, key):
        find = self.FindNodeByKey(key)
        if find.NodeHasKey is False:
            return False
        self.Root = self._DeleteNodeByKey(self.Root, key)
        return True


    def Count(self):
        if self.Root is None:
            return 0
        return self._Count(self.Root, 1)
        
    
    def _Count(self, node, count):
        if node.LeftChild is not None:
            count = self._Count(node.LeftChild, count + 1)
        if node.RightChild is not None:
            count = self._Count(node.RightChild, count + 1)
        return count
    
    def WideAllNodes(self):
        nodes = ()
        if self.Root is None:
            return nodes
        parents = [self.Root]
        nodes = nodes + (self.Root,)
        return self._WideAllNodes(parents, nodes)

    def _WideAllNodes(self, parents, nodes):
        new_parents = []
        for el in parents:
            if el.LeftChild is not None:
                nodes += (el.LeftChild,)
                new_parents.append(el.LeftChild)
            if el.RightChild is not None:
                nodes += (el.RightChild,)
                new_parents.append(el.RightChild)
        if len(new_parents) == 0:
            return nodes
        return self._WideAllNodes(new_parents, nodes)


        

        
