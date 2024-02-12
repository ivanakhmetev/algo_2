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
  
    # def FinMinMax(self, FromNode, FindMax):
    #     # return self._FindMin2(FromNode, FindMax)
    #     if FromNode is None:
    #         return BSTFind()
    #     if FindMax is True:
    #         return self._FindMax(FromNode)
    #     if FindMax is False:
    #         return self._FindMin(FromNode)
        

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
    
    # def _FindMin(self, node):
    #     if node.LeftChild is not None:# and node.RightChild is not None and node.LeftChild.NodeValue < node.RightChild.NodeValue:
    #         return self._FindMin(node.LeftChild)
    #     # if node.LeftChild is None and node.RightChild is not None:
    #     #     return self._FindMin(node.RightChild)
    #     find = BSTFind()
    #     if node is not None:
    #         find.Node = node
    #         find.NodeHasKey = True
    #     return find

    # def _FindMax(self, node):
    #     if node.RightChild is not None:
    #         return self._FindMax(node.RightChild)
    #     # if node.RightChild is None and node.LeftChild is not None: 
    #     #     return self._FindMax(node.LeftChild)
    #     find = BSTFind()
    #     if node is not None:
    #         find.Node = node
    #         find.NodeHasKey = True
    #     return find

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return BSTNode(None, None, None)
            # return BSTFind()  # Возвращаем пустой результат поиска

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



	
    # def DeleteNodeByKey(self, key):
    #     find = self.FindNodeByKey(key)
    #     if find.NodeHasKey is False:
    #         return False
    #     node = find.Node
    #     if node == self.Root and self.IsLeaf(node):
    #         self.Root = None
    #         return True
    #     if node == self.Root and self.HasSingleLeftChild(node):
    #         self.Root = node.LeftChild
    #         self.Root.Parent = None
    #         return True
    #     if node == self.Root and self.HasSingleRightChild(node):
    #         self.Root = node.RightChild
    #         self.Root.Parent = None
    #         return True
    #     if node == self.Root and self.HasBothChilds(node):
    #         min_find = self.FinMinMax(node.RightChild, False)
    #         if self.IsLeaf(min_find):
    #             self.Root = min_find
    #             self.Root.Parent = None
    #             return True
    #         if self.HasSingleRightChild(min_find):
    #             min_find.Parent.LeftChild = min_find.RightChild
    #             self.Root = min_find
    #             self.Root.Parent = None
    #             return True
                        
    #     if self.IsLeaf(node) and self.IsLeftChild(node):
    #         node.Parent.LeftChild = None
    #         return True
    #     if self.IsLeaf(node) and self.IsRightChild(node):
    #         node.Parent.RightChild = None
    #         return True
    #     if self.HasSingleLeftChild(node) and self.IsLeftChild(node):
    #         node.Parent.LeftChild = node.LeftChild
    #         return True
    #     if self.HasSingleLeftChild(node) and self.IsRightChild(node):
    #         node.Parent.RightChild = node.LeftChild
    #         return True
    #     if self.HasSingleRightChild(node) and self.IsLeftChild(node):
    #         node.Parent.LeftChild = node.RightChild
    #         return True
    #     if self.HasSingleRightChild(node) and self.IsRightChild(node):
    #         node.Parent.RightChild = node.RightChild
    #         return True

    #     min_find = self.FinMinMax(node.RightChild, False)
    #     if self.IsLeaf(min_find) and self.IsLeftChild(node):
    #         node.Parent.LeftChild = min_find
    #         return True
    #     if self.IsLeaf(min_find) and self.IsRightChild(node):
    #         node.Parent.RightChild = min_find
    #         return True
    #     if self.HasSingleRightChild(min_find) and self.IsLeftChild(node):
    #         node.Parent.LeftChild = min_find
    #         min_find.Parent.LeftChild = min_find.RightChild
    #         return True
    #     if self.HasSingleRightChild(min_find) and self.IsRightChild(node):
    #         node.Parent.RightChild = min_find
    #         min_find.Parent.LeftChild = min_find.RightChild
    #         return True

    # def DeleteNodeByKey(self, key):
    #     find = self.FindNodeByKey(key)
    #     if find.NodeHasKey is False:
    #         return False

    #     node = find.Node
    #     parent = node.Parent

    #     # Определяем, является ли узел листом
    #     is_leaf = self.IsLeaf(node)

    #     # Удаление корневого узла
    #     if node == self.Root:
    #         if is_leaf:
    #             self.Root = None
    #         elif self.HasSingleLeftChild(node):
    #             self.Root = node.LeftChild
    #             node.LeftChild.Parent = None
    #         elif self.HasSingleRightChild(node):
    #             self.Root = node.RightChild
    #             node.RightChild.Parent = None
    #         else:
    #             min_find = self.FinMinMax(node.RightChild, False)
    #             min_node = min_find.Node
    #             if self.IsLeaf(min_node):
    #                 min_node.Parent.LeftChild = None
    #             else:
    #                 min_node.Parent.LeftChild = min_node.RightChild
    #                 min_node.RightChild.Parent = min_node.Parent
    #             self.Root = min_node
    #             min_node.Parent = None
    #         return True

    #     # Удаление узла, который не является корневым
    #     if is_leaf:
    #         if self.IsLeftChild(node):
    #             parent.LeftChild = None
    #         else:
    #             parent.RightChild = None
    #     elif self.HasSingleLeftChild(node):
    #         if self.IsLeftChild(node):
    #             parent.LeftChild = node.LeftChild
    #         else:
    #             parent.RightChild = node.LeftChild
    #         node.LeftChild.Parent = parent
    #     elif self.HasSingleRightChild(node):
    #         if self.IsLeftChild(node):
    #             parent.LeftChild


    def IsLeftChild(self, node):
        if node.Parent is not None and node.Parent.LeftChild == node:
            return True
        return False
    
    def IsRightChild(self, node):
        if node.Parent is not None and node.Parent.RightChild == node:
            return True
        return False


    def IsLeaf(self, node):
        if node.LeftChild is None and node.RightChild is None:
            return True
        return False
    
    def HasBothChilds(self, node):
        if node.LeftChild is not None and node.RightChild is not None:
            return True
        return False

    
    def HasSingleLeftChild(self, node):
        if node.LeftChild is not None and node.RightChild is None:
            return True
        return False
    
    def HasSingleRightChild(self, node):
        if node.LeftChild is None and node.RightChild is not None:
            return True
        return False


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
